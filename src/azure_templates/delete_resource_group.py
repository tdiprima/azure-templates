# Script to delete an Azure Resource Group (and all resources inside it).
# WARNING: This is destructive; use with caution.

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # RG to delete

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
