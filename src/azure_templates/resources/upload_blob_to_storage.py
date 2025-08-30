# Script to upload a file as a blob to Azure Blob Storage.
# Requires an existing storage account and container.

import os

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
container_name = os.getenv("AZURE_CONTAINER_NAME")
blob_name = os.getenv("AZURE_BLOB_NAME")
local_file_path = os.getenv("LOCAL_FILE_PATH")

# Authenticate and connect
account_url = f"https://{storage_account_name}.blob.core.windows.net"
credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential=credential)

try:
    # Get container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create container if it doesn't exist
    if not container_client.exists():
        container_client.create_container()

    # Upload the blob
    with open(local_file_path, "rb") as data:
        blob_client = container_client.upload_blob(
            name=blob_name, data=data, overwrite=True
        )
    print(f"Blob '{blob_name}' uploaded to container '{container_name}'.")
except Exception as e:
    print(f"Error uploading blob: {e}")
