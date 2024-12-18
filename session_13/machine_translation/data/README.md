# **Data Processing for Translation Project**

This directory contains scripts and folders for processing and organizing the dataset required for machine translation projects. Below is an explanation of each folder and Python script.

## **Directory Structure**
```bash
data/
│
├── processed/                  # Folder to store processed data.
│
├── raw/                        # Folder to store raw, unprocessed data.
│
├── download_opus_books.py      # Script to download the OPUS Books dataset.
│
├── preprocess_translation_data.py  # Script to preprocess translation data.
│
└── README.md                   # Documentation file.
```

## **Folder Descriptions**

### `processed/`
- This folder is where the processed data will be stored.  
- Processed data is cleaned and formatted for model training.

### `raw/`
- Contains raw, unprocessed datasets downloaded from external sources.  
- Typically includes text files or other original formats for machine translation.

### `download_opus_books.py`
- **Purpose**: Downloads the OPUS Books dataset, a popular resource for translation tasks.  
- **Details**:
  - Retrieves text data in multiple languages.
  - Stores the downloaded data in the `raw/` folder.
- **Usage**:  
   Run the script as follows:
   ```bash
   python download_opus_books.py
   ```

### `preprocess_translation_data.py`
- **Purpose**: Cleans and preprocesses the raw text data to prepare it for training.  
- **Steps**:
  1. Reads data from the `raw/` folder.
  2. Tokenizes, filters, and formats the text.
  3. Saves the preprocessed data into the `processed/` folder.
- **Usage**:  
   Run the script as follows:
   ```bash
   python preprocess_translation_data.py
   ```
