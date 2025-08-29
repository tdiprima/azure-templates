# Script to list all resources in a Resource Group.

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # RG to query

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
