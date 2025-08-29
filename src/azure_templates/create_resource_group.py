# Script to create a new Azure Resource Group.
# Use as a template for organizing resources.

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # Desired RG name
location = "eastus"  # Azure region (e.g., 'westus', 'eastus')

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
