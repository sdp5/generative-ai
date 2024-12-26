
# ! pip install -q "evaluate==0.4.3"
# ! pip install -q "scikit-learn==1.6.0"

DEVICE = "cpu"
DATASET = "stanfordnlp/imdb"
DATASET_SEED = 23
SUBSET_SIZE = 100
PRETRAINED_MODEL = "distilbert-base-uncased"
FINE_TUNED_MODEL = "tashrifmahmud/sentiment_analysis_model_v2"
# PEFT_TECHNIQUE: LoRA
# EVALUATION_APPROACH: HuggingFace trainer.evaluate()

# -----------------------------------------
# Loading and Evaluating a Foundation Model
# -----------------------------------------

# LOADING THE MODEL

from datasets import load_dataset

# Load a dataset from the Hugging Face Hub.
dataset_splits = ["train", "test"]
try:
    # Example: IMDB dataset for sequence classification
    loaded_dataset = load_dataset(DATASET, split=dataset_splits)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
else:
    datasets = {split: ds for split, ds in zip(dataset_splits, loaded_dataset)}

# Take a subset of the dataset to reduce computational resources
try:
    # Thin out the dataset to make it run faster for this example.
    for split in dataset_splits:
        datasets[split] = datasets[split].shuffle(seed=DATASET_SEED).select(range(SUBSET_SIZE))
    print("Subset of the dataset created successfully.")
except Exception as e:
    print(f"An error occurred while creating a subset of the dataset: {e}")
else:
    print("Train split of dataset:")
    print(datasets["train"])

    print("Test split of dataset:")
    print(datasets["test"])

    print("Let's take a look at first data in the set:")
    print(datasets["train"][0])

# Load the tokenizer for the pretrained model.
from transformers import AutoTokenizer

try:
    pre_trained_tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL)
    fine_tuned_tokenizer = AutoTokenizer.from_pretrained(FINE_TUNED_MODEL)
    print("Tokenizers loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the tokenizers: {e}")

# Tokenize both the dataset subsets: train and test.
def preprocess_function(examples):
    """Preprocess the imdb dataset by returning tokenized examples"""
    return pre_trained_tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_ds = {}
try:
    for split in dataset_splits:
        tokenized_ds[split] = datasets[split].map(preprocess_function, batched=True)
    print("Dataset tokenized successfully.")
except Exception as e:
    print(f"An error occurred while tokenizing the dataset: {e}")
else:
    # Check that we tokenized the examples properly
    assert tokenized_ds["train"][0]["input_ids"][:5] == [101, 2004, 2574, 2004, 1045]

    print("Show the first example of tokenized training set:")
    print(tokenized_ds["train"][0]["input_ids"])

# Load the pretrained model for sequence classification
from transformers import AutoModelForSequenceClassification, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_storage=torch.bfloat16,
)

try:
    pre_trained_model = AutoModelForSequenceClassification.from_pretrained(
        PRETRAINED_MODEL,
        # quantization_config=bnb_config,
        # torch_dtype=torch.bfloat16,
        num_labels=2,
        id2label={0: "NEGATIVE", 1: "POSITIVE"},  # For converting predictions to strings
        label2id={"NEGATIVE": 0, "POSITIVE": 1},
    )
    print("Pretrained Model loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
else:
    pre_trained_model.to(DEVICE)

# Load the fine-tuned model for sequence classification
try:
    fine_tuned_model = AutoModelForSequenceClassification.from_pretrained(
        FINE_TUNED_MODEL, num_labels=2,
        id2label={0: "NEGATIVE", 1: "POSITIVE"},
        label2id={"NEGATIVE": 0, "POSITIVE": 1},
    )
    print("Fine tuned Model loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
else:
    fine_tuned_model.to(DEVICE)

# Unfreeze all the model parameters.
# Hint: Check the documentation at https://huggingface.co/transformers/v4.2.2/training.html
for param in pre_trained_model.base_model.parameters():
    param.requires_grad = True

print("Pretrained Model classifiers:")
print(pre_trained_model.classifier)

print("Inspect Pretrained Model:")
print(pre_trained_model)

print("Fine Tuned Model classifiers:")
print(fine_tuned_model.classifier)

print("Inspect Fine Tuned Model:")
print(fine_tuned_model)

# EVALUATING THE MODEL

import numpy as np
from transformers import DataCollatorWithPadding, Trainer, TrainingArguments

# Helper function to compute prediction accuracy
def compute_metrics(eval_predictions):
    e_predictions, e_labels = eval_predictions
    e_predictions = np.argmax(e_predictions, axis=1)
    return {"accuracy": (e_predictions == e_labels).mean()}

# The HuggingFace Trainer class handles the training and eval loop for PyTorch for us.
# Read more about it here https://huggingface.co/docs/transformers/main_classes/trainer
trainer = Trainer(
    model=pre_trained_model,
    args=TrainingArguments(
        output_dir="./data/sentiment_analysis/pre_trained/",
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
    tokenizer=pre_trained_tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=pre_trained_tokenizer),
    compute_metrics=compute_metrics,
)

print("Evaluate pre-trained foundation_model.")
pre_train_evaluate_results = trainer.evaluate()
print(pre_train_evaluate_results)

print("Full train the foundation_model.")
trainer.train()

print("Evaluate post-trained foundation_model.")
post_train_evaluate_results = trainer.evaluate()
print(post_train_evaluate_results)

# The HuggingFace Trainer class for the fine_tuned_model.
trainer_ft = Trainer(
    model=fine_tuned_model,
    args=TrainingArguments(
        output_dir="./data/sentiment_analysis/fine_tuned/",
        learning_rate=2e-3,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        num_train_epochs=1,
        weight_decay=0.01,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    ),
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["test"],
    tokenizer=fine_tuned_tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=fine_tuned_tokenizer),
    compute_metrics=compute_metrics,
)

print("Evaluate fine-tuned pre-trained model.")
fine_tuned_evaluate_results = trainer_ft.evaluate()
print(fine_tuned_evaluate_results)

# Show some of the predictions.
import pandas as pd

df = pd.DataFrame(tokenized_ds["test"])
df = df[["text", "label"]]

# Replace <br /> tags in the text with spaces.
df["text"] = df["text"].str.replace("<br />", " ")

# Add the model predictions to the dataframe.
predictions = trainer.predict(tokenized_ds["test"])
df["predicted_label"] = np.argmax(predictions[0], axis=1)

print(df.head(10))

print("Look at some of the incorrect predictions.")
print(df[df["label"] != df["predicted_label"]].head(10))

# ------------------------------------------
# Performing Parameter-Efficient Fine-Tuning
# ------------------------------------------

# CREATING A PEFT CONFIG

# Create a PEFT config with appropriate hyperparameters for the chosen model.
from peft import get_peft_model, LoraConfig, TaskType

# Set up a LoRA config
peft_config_seq_cls = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    inference_mode=False,
    r=8,
    target_modules=["q_lin", "v_lin"],
    lora_alpha=32,
    lora_dropout=0.1,
)

# CREATING A PEFT MODEL

# Using the PEFT config and foundation model, create a PEFT model.
peft_model_seq_cls = get_peft_model(pre_trained_model, peft_config_seq_cls)
peft_model_seq_cls.to(DEVICE)
peft_model_seq_cls.print_trainable_parameters()

print("PEFT SEQ_CLS MODEL:")
print(peft_model_seq_cls)

# TRAINING THE MODEL

import numpy as np
from transformers import DataCollatorWithPadding, Trainer, TrainingArguments

# The HuggingFace Trainer class handles the training and eval loop for PyTorch for us.
# Read more about it here https://huggingface.co/docs/transformers/main_classes/trainer
peft_trainer_seq_cls = Trainer(
    model=peft_model_seq_cls,
    args=TrainingArguments(
        output_dir="./data/sentiment_analysis/peft_seq_cls/",
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
    tokenizer=pre_trained_tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=pre_trained_tokenizer),
    compute_metrics=compute_metrics,
)

# Evaluate pre-trained lightweight fine-tuned model.
peft_seq_cls_pre_train_evaluate_results = peft_trainer_seq_cls.evaluate()
print(f"peft_seq_cls_pre_train_results: {peft_seq_cls_pre_train_evaluate_results}")

# Train the lightweight fine-tuned model.
peft_trainer_seq_cls.train()

# Evaluate the lightweight fine-tuned model post training.
peft_seq_cls_post_train_evaluate_results = peft_trainer_seq_cls.evaluate()
print(f"peft_seq_cls_post_train_results: {peft_seq_cls_post_train_evaluate_results}")

# Show some of the predictions.

import pandas as pd

df = pd.DataFrame(tokenized_ds["test"])
df = df[["text", "label"]]

# Replace <br /> tags in the text with spaces
df["text"] = df["text"].str.replace("<br />", " ")

# Add the model predictions to the dataframe
predictions = peft_trainer_seq_cls.predict(tokenized_ds["test"])
df["predicted_label"] = np.argmax(predictions[0], axis=1)

print(df.head(10))

# SAVING THE TRAINED MODEL

peft_model_seq_cls.save_pretrained("./data/peft_model/seq_cls/")

# --------------------------------------
# Performing Inference with a PEFT Model
# --------------------------------------

# LOADING THE MODEL

from peft import PeftModel, PeftConfig, AutoPeftModelForSequenceClassification

# Load model and config from the persist storage.
peft_seq_cls_model_path = "./data/peft_model/seq_cls/"
peft_config = PeftConfig.from_pretrained(peft_seq_cls_model_path)

saved_peft_seq_cls_model = AutoPeftModelForSequenceClassification.from_pretrained(peft_seq_cls_model_path)
saved_peft_seq_cls_model.to(DEVICE)

print("Reconstructed model from saved PEFT:")
print(saved_peft_seq_cls_model)

# Load AutoTokenizer
peft_tokenizer = AutoTokenizer.from_pretrained(peft_config.base_model_name_or_path)
items_indexes_for_manual_review = [0, 1, 13, 25, 46, 51, 64, 88, 90, 94, 95, 99]

# EVALUATING THE MODEL

test_items = tokenized_ds["test"].select(
    items_indexes_for_manual_review
)

# Print test_items columns.
print(test_items)

# Inspect test items and input_ids.
for test_item in test_items:
    print(test_item['input_ids'])
    print(test_item)
    break

# Make a dataframe with the predictions and the text and the labels.
import pandas as pd
import torch

items_for_manual_review = tokenized_ds["test"].select(
    items_indexes_for_manual_review
)

predictions = []
for i in items_for_manual_review:
    input_tokens = peft_tokenizer(i['text'], return_tensors="pt")
    with torch.no_grad():
        logits = saved_peft_seq_cls_model(**input_tokens).logits
        predicted_class_id = logits.argmax().item()
        predictions.append(predicted_class_id)

print(predictions)

# Table text, prediction and labels for the selected items.
df = pd.DataFrame(
    {
        "text": [item["text"] for item in items_for_manual_review],
        "predictions": predictions,
        "labels": [item["label"] for item in items_for_manual_review],
    }
)
print(df)

# Deduce labels of the selected items.
labels = [item["label"] for item in items_for_manual_review]

import evaluate

accuracy_metric = evaluate.load("accuracy")
results = accuracy_metric.compute(references=labels, predictions=predictions)
print(results)

# SHOW PERFORMANCE IMPROVEMENTS

df = pd.DataFrame(
    {
        "stage": [
            "Foundation model before training",
            "Foundation model after training",
            "PEFT model before training",
            "PEFT model after training",
            "Fine tuned trained model",
        ],
        "details": [
            PRETRAINED_MODEL,
            PRETRAINED_MODEL,
            "PEFT LoRA SEQ_CLS Model",
            "PEFT LoRA SEQ_CLS Model",
            FINE_TUNED_MODEL,
        ],
        "eval_loss": map(lambda x: "{:.6f}".format(x), [
            pre_train_evaluate_results["eval_loss"],
            post_train_evaluate_results["eval_loss"],
            peft_seq_cls_pre_train_evaluate_results["eval_loss"],
            peft_seq_cls_post_train_evaluate_results["eval_loss"],
            fine_tuned_evaluate_results["eval_loss"],
        ]),
    }
)

# Print eval_loss results
print(df)

## Suggestions to Make Your Project Stand Out
# Try using the bitsandbytes package (installed in the workspace) to combine quantization and LoRA. This is also known as QLoRA
# Try training the model using different PEFT configurations and compare the results
