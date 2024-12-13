import requests
import zipfile
import os
import shutil

# Define the URL of the ZIP file
zip_url = "https://github.com/AsoSoft/AsoSoft-Text-Corpus/raw/master/AsoSoft%20Text%20Corpus%20Small%20Version/AsoSoft Text Corpus- Small Version 1.0 (2018-12-10).zip"

# Define the local filename
local_zip_file = "AsoSoft Text Corpus- Small Version 1.0 (2018-12-10).zip"

# Download the ZIP file
print("Downloading ZIP file...")
response = requests.get(zip_url)
if response.status_code == 200:
    with open(local_zip_file, "wb") as file:
        file.write(response.content)
    print("Download complete.")
else:
    print(f"Failed to download file: {response.status_code}")

# Unzip the file and rename the desired file
print("Extracting contents and renaming...")
with zipfile.ZipFile(local_zip_file, "r") as zip_ref:
    extract_dir = "data"  # Directory to extract contents
    os.makedirs(extract_dir, exist_ok=True)
    zip_ref.extractall(extract_dir)

    # Find and rename the text file
    for file_name in os.listdir(extract_dir):
        if file_name.endswith(".txt"):  # Adjust if the file extension is different
            old_file_path = os.path.join(extract_dir, file_name)
            new_file_path = os.path.join(extract_dir, "text_data.txt")
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file_name}' to 'text_data.txt'.")

# Optional: Clean up (delete the ZIP file)
os.remove(local_zip_file)
print("Temporary ZIP file deleted.")
