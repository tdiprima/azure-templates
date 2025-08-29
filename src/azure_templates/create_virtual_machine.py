# Script to create a basic Virtual Machine (VM) in Azure.
# Requires an existing VNet and subnet. This creates a simple Linux VM.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")
location = os.getenv("AZURE_LOCATION")
vm_name = os.getenv("AZURE_VM_NAME")
vnet_name = os.getenv("AZURE_VNET_NAME")
subnet_name = os.getenv("AZURE_SUBNET_NAME")
admin_username = os.getenv("AZURE_ADMIN_USERNAME")
admin_password = os.getenv("AZURE_ADMIN_PASSWORD")

# Authenticate
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)

try:
    # Create NIC (Network Interface Card)
    nic = network_client.network_interfaces.begin_create_or_update(
        resource_group_name,
        f"{vm_name}Nic",
        {
            "location": location,
            "ip_configurations": [
                {
                    "name": "ipconfig1",
                    "subnet": {
                        "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{vnet_name}/subnets/{subnet_name}"
                    },
                }
            ],
        },
    ).result()

    # Create VM
    vm = compute_client.virtual_machines.begin_create_or_update(
        resource_group_name,
        vm_name,
        {
            "location": location,
            "hardware_profile": {"vm_size": os.getenv("AZURE_VM_SIZE")},
            "storage_profile": {
                "image_reference": {
                    "publisher": "Canonical",
                    "offer": "0001-com-ubuntu-server-jammy",
                    "sku": "22_04-lts",
                    "version": "latest",
                }
            },
            "os_profile": {
                "computer_name": vm_name,
                "admin_username": admin_username,
                "admin_password": admin_password,
            },
            "network_profile": {"network_interfaces": [{"id": nic.id}]},
        },
    ).result()
    print(f"VM '{vm_name}' created successfully.")
except Exception as e:
    print(f"Error creating VM: {e}")
