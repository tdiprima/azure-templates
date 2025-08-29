# Script to create a Virtual Network (VNet) in Azure.
# Use as a template for networking setups.

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # Existing RG name
vnet_name = "myVNet"  # VNet name
location = "eastus"  # Azure region
address_prefix = "10.0.0.0/16"  # CIDR block for VNet

# Authenticate
credential = DefaultAzureCredential()
network_client = NetworkManagementClient(credential, subscription_id)

try:
    # Create the virtual network
    async_vnet_creation = network_client.virtual_networks.begin_create_or_update(
        resource_group_name,
        vnet_name,
        {"location": location, "address_space": {"address_prefixes": [address_prefix]}},
    )
    vnet_info = async_vnet_creation.result()
    print(
        f"Virtual Network '{vnet_name}' created with address space '{address_prefix}'."
    )
except Exception as e:
    print(f"Error creating virtual network: {e}")
