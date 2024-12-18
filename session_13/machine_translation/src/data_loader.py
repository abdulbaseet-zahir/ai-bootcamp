from datasets import DatasetDict, Dataset
from transformers import AutoTokenizer
import pandas as pd
import config


def load_and_preprocess_data(csv_paths=None):
    """
    Load preprocessed data from CSV files and tokenize for training.

    Args:
        csv_paths (dict): Dictionary with keys ('train', 'validation', 'test') pointing to CSV file paths.

    Returns:
        DatasetDict: Tokenized dataset compatible with HuggingFace transformers.
    """
    if csv_paths is None:
        csv_paths = config.CSV_PATHS
        csv_paths = {
            "train": "../data/processed/train.csv",
            "validation": "../data/processed/validation.csv",
            "test": "../data/processed/test.csv",
        }
    # Load CSV files into pandas DataFrames
    train_df = pd.read_csv(csv_paths["train"])
    val_df = pd.read_csv(csv_paths["validation"])
    test_df = pd.read_csv(csv_paths["test"])

    # Convert DataFrames to HuggingFace Dataset objects
    dataset_dict = DatasetDict(
        {
            "train": Dataset.from_pandas(train_df),
            "validation": Dataset.from_pandas(val_df),
            "test": Dataset.from_pandas(test_df),
        }
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config.TOKENIZER_NAME)

    # Tokenization function
    def tokenize_function(examples):
        return tokenizer(
            examples["English"],
            text_target=examples["German"],
            padding="max_length",
            max_length=128,
            truncation=True,
        )

    # Apply tokenization
    tokenized_dataset = dataset_dict.map(
        tokenize_function,
        batched=True,
        batch_size=16,
        remove_columns=["English", "German"],
    )

    return tokenized_dataset
