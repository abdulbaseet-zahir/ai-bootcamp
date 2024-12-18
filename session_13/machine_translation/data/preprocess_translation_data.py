import pandas as pd
import re


def clean_text(text):
    """
    Clean text by removing special characters and multiple spaces.
    """
    text = re.sub(r"[^\w\s.,!?']+", "", text)  # Remove unwanted special characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text


def preprocess_data(file_paths):
    """
    Load and preprocess translation datasets.

    Args:
        file_paths (dict): Dictionary with keys ('train', 'validation', 'test') and CSV file paths.

    Returns:
        dict: Preprocessed datasets (train, validation, test).
    """
    datasets = {}

    for split, path in file_paths.items():
        # Load the CSV file
        df = pd.read_csv(path)

        # Clean English and German texts
        df["English"] = df["English"].apply(clean_text)
        df["German"] = df["German"].apply(clean_text)

        # Remove empty rows
        df = df.dropna(subset=["English", "German"])

        datasets[split] = df

    return datasets


def save_processed_datasets(datasets, output_dir="./processed"):
    """
    Save processed datasets as CSV files.

    Args:
        datasets (dict): Dictionary with processed DataFrames.
        output_dir (str): Directory to save processed files.
    """
    import os

    os.makedirs(output_dir, exist_ok=True)

    for split, df in datasets.items():
        output_path = f"{output_dir}/{split}.csv"
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"Saved processed {split} dataset to {output_path}")


if __name__ == "__main__":
    # Define paths to the original datasets
    file_paths = {
        "train": "./raw/opus_books_train.csv",
        "validation": "./raw/opus_books_validation.csv",
        "test": "./raw/opus_books_test.csv",
    }

    # Load and preprocess the datasets
    datasets = preprocess_data(file_paths)

    # Save preprocessed datasets
    save_processed_datasets(datasets, output_dir="./processed")
