import os
from datasets import load_dataset
import pandas as pd


def download_and_save_opus_books():
    """
    Load the opus_books dataset and save it as CSV files. So it's easier to understan how we can process the raw data.
    """
    # Load the opus_books dataset with the correct configuration
    train_dataset = load_dataset("opus_books", "de-en", split="train[:90%]")
    val_dataset = load_dataset("opus_books", "de-en", split="train[90%:95%]")
    test_dataset = load_dataset("opus_books", "de-en", split="train[95%:100%]")

    output_path = "./raw"
    os.makedirs(output_path, exist_ok=True)

    # Convert the dataset splits to pandas DataFrames
    # Invert the columns for English as source and German as target
    train_data = pd.DataFrame(train_dataset["translation"])[:3_000]
    val_data = pd.DataFrame(val_dataset["translation"])[:1_000]
    test_data = pd.DataFrame(test_dataset["translation"])[:1_000]

    # Rename columns to match the desired format (English -> German)
    train_data = train_data.rename(columns={"de": "German", "en": "English"})
    val_data = val_data.rename(columns={"de": "German", "en": "English"})
    test_data = test_data.rename(columns={"de": "German", "en": "English"})

    # Save each split to CSV files
    train_data.to_csv(
        f"{output_path}/opus_books_train.csv", index=False, encoding="utf-8"
    )
    val_data.to_csv(
        f"{output_path}/opus_books_validation.csv", index=False, encoding="utf-8"
    )
    test_data.to_csv(
        f"{output_path}/opus_books_test.csv", index=False, encoding="utf-8"
    )

    print("Datasets saved as CSV:")
    print(" - opus_books_train.csv")
    print(" - opus_books_validation.csv")
    print(" - opus_books_test.csv")


# Run the function
if __name__ == "__main__":
    download_and_save_opus_books()
