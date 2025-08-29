# Script to create a basic Virtual Machine (VM) in Azure.
# Requires an existing VNet and subnet. This creates a simple Linux VM.

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # Existing RG name
location = "eastus"  # Azure region
vm_name = "myVM"  # VM name
vnet_name = "myVNet"  # Existing VNet name
subnet_name = "mySubnet"  # Subnet name (create if needed)
admin_username = "azureuser"  # VM admin username
admin_password = "P@ssw0rd123!"  # VM admin password (use SSH keys in production)

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
            "hardware_profile": {"vm_size": "Standard_DS1_v2"},  # VM size
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
