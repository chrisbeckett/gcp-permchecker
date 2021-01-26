# Simple GCP Permissions Checker Tool

This tool checks the GCP IAM permissions of a service account.

# How to use

You need :-

- Python 3.8 or higher
- Git
- GCP Service Account JSON credentials file
- An environment variable called **GOOGLE_APPLICATION_CREDENTIALS** pointing to your JSON file *(example : GOOGLE_APPLICATION_CREDENTIALS="mycreds.json")*

# Installation steps

- **git clone https://github.com/chrisbeckett/gcp-permchecker.git**
- **python3 -m venv gcp-permchecker**
- **cd gcp-permchecker**
- **bin/activate.bat (Windows) or source bin/activate (Mac/Linux)**
- **pip install -r requirements.txt**
- **python3 gcp-permchecker.py**
