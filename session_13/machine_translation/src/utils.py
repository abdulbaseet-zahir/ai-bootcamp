def print_model_params(model):
    print(f"{model.num_parameters():,} trainable parameters")


def move_model_folder(src, dst):
    import shutil
    import os

    # Define the source and destination paths
    PRETRAINED_MODEL = src
    PRETRAINED_MODEL_API = dst

    # Check if the source directory exists
    if os.path.exists(PRETRAINED_MODEL):
        # Create the destination directory if it doesn't exist
        os.makedirs(PRETRAINED_MODEL_API, exist_ok=True)

        # Move the directory
        try:
            shutil.move(PRETRAINED_MODEL, PRETRAINED_MODEL_API)
            print(f"Model moved from {PRETRAINED_MODEL} to {PRETRAINED_MODEL_API}")
        except Exception as e:
            print(f"Error moving the model: {e}")
    else:
        print(f"Source path {PRETRAINED_MODEL} does not exist.")
