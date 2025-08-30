# Script to create an Azure Storage Account.
# Use as a template for blob, file, or queue storage.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")
storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
location = os.getenv("AZURE_LOCATION")
sku = os.getenv("AZURE_STORAGE_SKU")

# Authenticate
credential = DefaultAzureCredential()
storage_client = StorageManagementClient(credential, subscription_id)

try:
    # Create the storage account
    storage_async_operation = storage_client.storage_accounts.begin_create(
        resource_group_name,
        storage_account_name,
        {
            "location": location,
            "sku": {"name": sku},
            "kind": "StorageV2",  # General-purpose v2
        },
    )
    storage_account = storage_async_operation.result()
    print(f"Storage Account '{storage_account_name}' created in '{location}'.")
except Exception as e:
    print(f"Error creating storage account: {e}")
