# Script to create a new Azure Resource Group.
# Use as a template for organizing resources.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")
location = os.getenv("AZURE_LOCATION")

# Authenticate
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

try:
    # Create the resource group
    rg_result = resource_client.resource_groups.create_or_update(
        resource_group_name, {"location": location}
    )
    print(f"Resource Group '{resource_group_name}' created in '{location}'.")
except Exception as e:
    print(f"Error creating resource group: {e}")
