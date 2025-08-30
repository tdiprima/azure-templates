# Script to delete an Azure Resource Group (and all resources inside it).
# WARNING: This is destructive; use with caution.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")

# Authenticate
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

try:
    # Delete the resource group
    delete_async_operation = resource_client.resource_groups.begin_delete(
        resource_group_name
    )
    delete_async_operation.wait()  # Wait for completion
    print(f"Resource Group '{resource_group_name}' deleted successfully.")
except Exception as e:
    print(f"Error deleting resource group: {e}")
