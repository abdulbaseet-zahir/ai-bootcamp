import os
from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainer, Seq2SeqTrainingArguments
import config
import data_loader
import utils


def train_model(tokenized_dataset):
    """
    Trains a sequence-to-sequence language model on a given tokenized dataset.

    Args:
        tokenized_dataset (dict): A dictionary containing the tokenized training and validation datasets.
            Expected keys: "train" and "validation".

    Returns:
        None

    Notes:
        This function assumes that the necessary configuration settings are defined in the `config` module,
        including `TOKENIZER_NAME`, `MODEL_PATH`, `CHECKPOINTS_DIR`, `BATCH_SIZE`, `EPOCHS`, and `PRETRANIDED_MODEL`.
    """
    model = AutoModelForSeq2SeqLM.from_pretrained(config.TOKENIZER_NAME)
    utils.print_model_params(model)
    output_dir = config.CHECKPOINTS_DIR
    os.makedirs(output_dir, exist_ok=True)
    training_args = Seq2SeqTrainingArguments(
        output_dir=config.CHECKPOINTS_DIR,
        eval_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=config.BATCH_SIZE,
        num_train_epochs=config.EPOCHS,
        logging_steps=200,
        report_to="none",
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["validation"],
    )

    trainer.train()
    os.makedirs(config.PRETRANIDED_MODEL, exist_ok=True)
    model.save_pretrained(config.PRETRANIDED_MODEL)


if __name__ == "__main__":
    tokenized_dataset = data_loader.load_and_preprocess_data()
    print("Dataset loaded and preprocessed successfully.")

    train_model(tokenized_dataset)
    print("Model training completed.")

    # Define the source and destination paths
    PRETRAINED_MODEL = "../models/saved_models/t5-en-de/"
    PRETRAINED_MODEL_API = "../api/"

    utils.move_model_folder(PRETRAINED_MODEL, PRETRAINED_MODEL_API)
