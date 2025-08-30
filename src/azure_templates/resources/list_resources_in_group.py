# Script to list all resources in a Resource Group.

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
    # List resources
    resources = resource_client.resources.list_by_resource_group(resource_group_name)
    for resource in resources:
        print(
            f"Resource Name: {resource.name}, Type: {resource.type}, Location: {resource.location}"
        )
    if not list(resources):
        print("No resources found in the resource group.")
except Exception as e:
    print(f"Error listing resources: {e}")
