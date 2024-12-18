# Machine Translation

This repository/folder implements an English-to-German machine translation system using a fine-tuned T5 model. It contains scripts for downloading, preprocessing, training, serving, and interacting with the translation model.

## Directory Structure

```bash
machine-translation/
│
├── data/
│   ├── raw/                 # Raw datasets (e.g., English-German parallel corpus)
│   ├── processed/           # Preprocessed datasets for training
│   └── README.md            # Description of dataset preparation
│
├── src/
│   ├── data_loader.py       # Scripts for loading and preprocessing datasets
│   ├── train.py             # Script for training the translation model
│   ├── infer.py             # Script for inference with the trained model
│   ├── utils.py             # Helper functions
│   └── config.py            # Configurations for training and deployment
│
├── models/
│   ├── saved_models/        # Directory for saving trained models
│   └── checkpoints/         # Checkpoints for intermediate model training stages
│
├── api/
│   ├── app.py               # FastAPI app for serving the model
│   └── requirements.txt     # Dependencies for the FastAPI service
│
├── gradio_app/
│   ├── app.py               # Gradio interface for user interaction
│   └── requirements.txt     # Dependencies for the Gradio app
│
├── notebooks/               # Jupyter notebooks for experimentation
│   └── exploration.ipynb
│
├── tests/                   # Unit tests for code
│   └── test_train.py
│
├── Dockerfile               # For containerizing the application
├── .gitignore               # Ignored files and folders in version control
├── README.md                # Project description and usage
└── requirements.txt         # Project-wide dependencies
```

### **Root Directory: `machine_translation`**
The root directory contains the main components of the project, including the following key subdirectories:

---

### **1. `src/` Directory**
This directory contains the core implementation of the project:
- **`train.py`**: Script to fine-tune the T5 model on the English-to-German dataset. The trained models are saved in the `models/saved_models/` directory.

---

### **2. `test/` Directory**
Contains unit and integration tests to verify the correctness of the implementation. Use these scripts to ensure the functionality of the data processing and model training workflows.

---

### **3. `notebooks/` Directory**
This directory contains Jupyter notebooks for exploratory data analysis (EDA), visualizations, and experiments with the dataset and the translation model.

---

### **4. `data/` Directory**
This directory contains scripts for handling the dataset:
- **`download_opus_books.py`**: Downloads the English-to-German dataset and saves it as a CSV file.
- **`preprocess_translation_data.py`**: Processes the downloaded dataset to prepare it for model training.

---

## Workflow

### **Step 1: Download the Dataset**
Run the following script to download the dataset:
```bash
cd data
python download_opus_books.py
```

### **Step 2: Preprocess the Dataset**
Preprocess the dataset for training:
```bash
cd data
python preprocess_translation_data.py
```

### **Step 3: Train the Model**
Train the T5 model with the preprocessed dataset:
```bash
cd src
python train.py
```
The trained model will be saved in the directory:
```
models/saved_models/t5-en-de
```

You can move this directory to the `api/` folder to be used by the FastAPI application.

---

## Running the Applications

### **1. Running the FastAPI API**
The FastAPI service provides a RESTful endpoint to access the translation model. To run the API:

```bash
cd api
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

### **2. Running the Gradio Application**
The Gradio app provides a user-friendly interface for translating English text to German. To run the Gradio app:

```bash
cd gradio_app
python app.py
```
The Gradio interface will be available at `http://127.0.0.1:7860`.

---

### **3. Running the Application with Docker Compose**
You can also run both the FastAPI and Gradio applications using Docker Compose. From the root directory, run:

```bash
docker-compose up
```

This will start both services. FastAPI will be available at `http://127.0.0.1:8000` and Gradio at `http://127.0.0.1:7860`.

---

## Testing the Setup
You can test the FastAPI endpoint using the `/translate` endpoint to translate text:
- Example: `POST` request with `"text": "hello world"`.

You can interact with the Gradio app for a graphical user interface to perform translations.

