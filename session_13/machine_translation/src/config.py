# config.py

# General Settings
APP_NAME = "Machine Translation App"
APP_VERSION = "1.0.0"

# FastAPI Settings
HOST = "127.0.0.1"
PORT = 8000

# Dataset Settings
RAW_DATA_DIR = "../data/raw/"
PROCESSED_DATA_DIR = "../data/processed/"
CSV_PATHS = csv_paths = {
    "train": "../data/processed/train.csv",
    "validation": "../data/processed/validation.csv",
    "test": "../data/processed/test.csv",
}

# Model Settings
CHECKPOINTS_DIR = "../models/saved_models/checkpoints/"
PRETRANIDED_MODEL = "../models/saved_models/t5-en-de/"
TOKENIZER_NAME = "t5-small"

# Model Training Settings
EPOCHS = 1
BATCH_SIZE = 16

# API Keys or Secrets (Use environment variables for sensitive data!)
API_KEY = "your-secret-api-key"

# Other Configurations
DEBUG = True
