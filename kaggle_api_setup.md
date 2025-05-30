# Setting Up the Kaggle API Key

To use the Kaggle API and download datasets programmatically, follow these steps:

1. Go to [kaggle.com](https://www.kaggle.com/) and log in.
2. Click your profile picture > **Account**.
3. Scroll to **API** section and click **"Create New API Token"**.
4. This will download a file named `kaggle.json`.

## Usage

1. Move `kaggle.json` into your project root (same level as this README).
2. Add it to `.gitignore`:
   ```bash
   echo "kaggle.json" >> .gitignore
