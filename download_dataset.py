import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_fer2013(destination_path="data"):
    dataset_slug = "msambare/fer2013"
    zip_path = os.path.join(destination_path, "fer2013.zip")

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading {dataset_slug} to {zip_path}...")
    api.dataset_download_files(dataset_slug, path=destination_path, unzip=False)

    print("Unzipping dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(destination_path)

    print("Done!")

if __name__ == "__main__":
    download_fer2013()
