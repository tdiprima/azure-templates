# Script to create a Virtual Network (VNet) in Azure.
# Use as a template for networking setups.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")
vnet_name = os.getenv("AZURE_VNET_NAME")
location = os.getenv("AZURE_LOCATION")
address_prefix = os.getenv("AZURE_ADDRESS_PREFIX")

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
