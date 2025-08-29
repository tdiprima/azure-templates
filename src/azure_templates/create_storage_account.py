# Script to create an Azure Storage Account.
# Use as a template for blob, file, or queue storage.

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # Existing RG name
storage_account_name = (
    "mystorageaccount123"  # Unique storage account name (globally unique, lowercase)
)
location = "eastus"  # Azure region
sku = "Standard_LRS"  # SKU (e.g., 'Standard_LRS', 'Premium_LRS')

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
