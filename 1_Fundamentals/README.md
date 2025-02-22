## Project: Apply Lightweight Fine-Tuning to a Foundation Model

### Loading and Evaluating a Foundation Model
#### Loading the model
Once you have selected a model, load it in your notebook.

#### Evaluating the model
Perform an initial evaluation of the model on your chosen sequence classification task. This step will require that you also load an appropriate tokenizer and dataset.

### Performing Parameter-Efficient Fine-Tuning
#### Creating a PEFT config
Create a PEFT config with appropriate hyperparameters for your chosen model.

#### Creating a PEFT model
Using the PEFT config and foundation model, create a PEFT model.

#### Training the model
Using the PEFT model and dataset, run a training loop with at least one epoch.

#### Saving the trained model
Depending on your training loop configuration, your PEFT model may have already been saved. If not, use `save_pretrained` to save your progress.

### Performing Inference with a PEFT Model
#### Loading the model
Using the appropriate PEFT model class, load your trained model.

#### Evaluating the model
Repeat the previous evaluation process, this time using the PEFT model. Compare the results to the results from the original foundation model.
