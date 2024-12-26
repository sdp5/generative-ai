#!/usr/bin/env python
# coding: utf-8

# # Lightweight Fine-Tuning Project

# TODO: In this cell, describe your choices for each of the following
# 
# * PEFT technique: LoRA
# * Model: distilbert-base-uncased
# * Evaluation approach: HuggingFace trainer.evaluate()
# * Fine-tuning dataset: stanfordnlp/imdb

# ## Loading and Evaluating a Foundation Model
# 
# TODO: In the cells below, load your chosen pre-trained Hugging Face model and evaluate its performance prior to fine-tuning. This step includes loading an appropriate tokenizer and dataset.

# In[1]:


get_ipython().system(' pip install -q "evaluate==0.4.3"')
get_ipython().system(' pip install -q "scikit-learn==1.6.0"')


# In[2]:


DEVICE = "cuda"
BASE_MODEL = "distilbert-base-uncased"
DATASET = "stanfordnlp/imdb"
# PEFT_TECHNIQUE: "LoRA"
# EVALUATION_APPROACH: HuggingFace trainer.evaluate()


# In[3]:


from datasets import load_dataset

dataset_splits = ["train", "test"]
loaded_dataset = load_dataset(DATASET, split=dataset_splits)
datasets = {split: ds for split, ds in zip(dataset_splits, loaded_dataset)}

# Thin out the dataset to make it run faster for this example
for split in dataset_splits:
    datasets[split] = datasets[split].shuffle(seed=23).select(range(250))

print("Train split of dataset:")
print(datasets["train"])

print("Test split of dataset:")
print(datasets["test"])

print("Let's take a look at first data in the set:")
print(datasets["train"][0])


# In[4]:


from transformers import AutoTokenizer
auto_tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

def preprocess_function(examples):
    """Preprocess the imdb dataset by returning tokenized examples"""
    return auto_tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_ds = {}
for split in dataset_splits:
    tokenized_ds[split] = datasets[split].map(preprocess_function, batched=True)

# Check that we tokenized the examples properly
assert tokenized_ds["train"][0]["input_ids"][:5] == [101, 2004, 2574, 2004, 1045]

print("Show the first example of tokenized training set:")
print(tokenized_ds["train"][0]["input_ids"])


# In[5]:


from transformers import AutoModelForSequenceClassification, AutoModelForCausalLM, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_storage=torch.bfloat16,
)

foundation_model = AutoModelForSequenceClassification.from_pretrained(
    BASE_MODEL,
    # quantization_config=bnb_config,
    # torch_dtype=torch.bfloat16,
    num_labels=2,
    id2label={0: "NEGATIVE", 1: "POSITIVE"},  # For converting predictions to strings
    label2id={"NEGATIVE": 0, "POSITIVE": 1},
)
foundation_model.to(DEVICE)

gpt_model = AutoModelForCausalLM.from_pretrained(
    "gpt2", num_labels=2,
    id2label={0: "NEGATIVE", 1: "POSITIVE"},
    label2id={"NEGATIVE": 0, "POSITIVE": 1},
)

# Unfreeze all the model parameters.
# Hint: Check the documentation at https://huggingface.co/transformers/v4.2.2/training.html
for param in foundation_model.base_model.parameters():
    param.requires_grad = True

print("Model classifiers:")
print(foundation_model.classifier)

print("Inspect Model:")
print(foundation_model)


# In[6]:


import numpy as np
from transformers import DataCollatorWithPadding, Trainer, TrainingArguments


def compute_metrics(eval_predictions):
    e_predictions, e_labels = eval_predictions
    e_predictions = np.argmax(e_predictions, axis=1)
    return {"accuracy": (e_predictions == e_labels).mean()}


# The HuggingFace Trainer class handles the training and eval loop for PyTorch for us.
# Read more about it here https://huggingface.co/docs/transformers/main_classes/trainer
trainer = Trainer(
    model=foundation_model,
    args=TrainingArguments(
        output_dir="./data/sentiment_analysis",
        learning_rate=2e-3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=1,
        weight_decay=0.01,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    ),
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["test"],
    tokenizer=auto_tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=auto_tokenizer),
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.evaluate()


# In[7]:


import pandas as pd

df = pd.DataFrame(tokenized_ds["test"])
df = df[["text", "label"]]

# Replace <br /> tags in the text with spaces
df["text"] = df["text"].str.replace("<br />", " ")

# Add the model predictions to the dataframe
predictions = trainer.predict(tokenized_ds["test"])
df["predicted_label"] = np.argmax(predictions[0], axis=1)

print(df.head(10))

print("Some of the incorrect predictions:")
print(df[df["label"] != df["predicted_label"]].head(10))


# ## Performing Parameter-Efficient Fine-Tuning
# 
# TODO: In the cells below, create a PEFT model from your loaded model, run a training loop, and save the PEFT model weights.

# In[8]:


from peft import get_peft_model, LoraConfig, TaskType


peft_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    inference_mode=False,
    r=8,
    target_modules=["q_lin", "v_lin"],
    lora_alpha=32,
    lora_dropout=0.1,
)

# Creating a PEFT model
# Using the PEFT config and foundation model, create a PEFT model.

# Creating a PEFT model
peft_model = get_peft_model(foundation_model, peft_config)
peft_model.to(DEVICE)
peft_model.print_trainable_parameters()

print("PEFT MODEL:")
print(peft_model)


# In[9]:


import numpy as np
from transformers import DataCollatorWithPadding, Trainer, TrainingArguments

# The HuggingFace Trainer class handles the training and eval loop for PyTorch for us.
# Read more about it here https://huggingface.co/docs/transformers/main_classes/trainer
peft_trainer = Trainer(
    model=peft_model,
    args=TrainingArguments(
        output_dir="./data/sentiment_analysis_peft",
        # Set the learning rate
        learning_rate=2e-5,
        # Set the per device train batch size and eval batch size
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        # Evaluate and save the model after each epoch
        evaluation_strategy="epoch",
        save_strategy="epoch",

        num_train_epochs=2,
        weight_decay=0.01,
        load_best_model_at_end=True,
    ),
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["test"],
    tokenizer=auto_tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=auto_tokenizer),
    compute_metrics=compute_metrics,
)

# Train the lightweight fine-tuned model
peft_trainer.train()


# In[10]:


# Evaluate the lightweight fine-tuned model
peft_trainer.evaluate()


# In[11]:


import pandas as pd

df = pd.DataFrame(tokenized_ds["test"])
df = df[["text", "label"]]

# Replace <br /> tags in the text with spaces
df["text"] = df["text"].str.replace("<br />", " ")

# Add the model predictions to the dataframe
predictions = trainer.predict(tokenized_ds["test"])
df["predicted_label"] = np.argmax(predictions[0], axis=1)

print(df.head(10))


# In[12]:


# Saving the trained model
peft_model.save_pretrained("./data/peft_model")


# ## Performing Inference with a PEFT Model
# 
# TODO: In the cells below, load the saved PEFT model weights and evaluate the performance of the trained PEFT model. Be sure to compare the results to the results from prior to fine-tuning.

# In[13]:


from peft import PeftModel, PeftConfig, AutoPeftModelForSequenceClassification

peft_model_path = "./data/peft_model"
peft_config = PeftConfig.from_pretrained(peft_model_path)

saved_peft_model = AutoPeftModelForSequenceClassification.from_pretrained(peft_model_path)
# saved_peft_model.to(DEVICE)

print("Reconstructed model from saved PEFT:")
print(saved_peft_model)


# In[14]:


peft_tokenizer = AutoTokenizer.from_pretrained(peft_config.base_model_name_or_path)
items_indexes_for_manual_review = \
    [0, 1, 13, 25, 46, 51, 64, 88, 90, 118, 125, 131, 148, 154, 166, 179, 183, 199, 222, 233, 244]

## Evaluating the model
test_items = tokenized_ds["test"].select(
    items_indexes_for_manual_review
)

# print test_items columns.
print(test_items)

# Inspect details.
for test_item in test_items:
    print(test_item['input_ids'])
    print(test_item)
    break


# In[15]:


import pandas as pd
import torch

items_for_manual_review = tokenized_ds["test"].select(
    items_indexes_for_manual_review
)

predictions = []
for i in items_for_manual_review:
    input_tokens = peft_tokenizer(i['text'], return_tensors="pt")
    with torch.no_grad():
        logits = saved_peft_model(**input_tokens).logits
        predicted_class_id = logits.argmax().item()
        predictions.append(predicted_class_id)

print(predictions)


# In[16]:


df = pd.DataFrame(
    {
        "text": [item["text"] for item in items_for_manual_review],
        "predictions": predictions,
        "labels": [item["label"] for item in items_for_manual_review],
    }
)
# Show all the cells
print(df)


# In[17]:


labels = [item["label"] for item in items_for_manual_review]


# In[18]:


# Let's evaluate accurancy.
import evaluate

accuracy_metric = evaluate.load("accuracy")
results = accuracy_metric.compute(references=labels, predictions=predictions)
print(results)

