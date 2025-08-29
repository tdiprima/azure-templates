# Script to list all Virtual Machines in a Resource Group.

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Replace with your values
subscription_id = "your-subscription-id"  # Azure Subscription ID
resource_group_name = "myResourceGroup"  # RG to query

# Authenticate
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

try:
    # List VMs
    vms = compute_client.virtual_machines.list(resource_group_name)
    for vm in vms:
        print(
            f"VM Name: {vm.name}, Location: {vm.location}, Size: {vm.hardware_profile.vm_size}"
        )
    if not list(vms):
        print("No VMs found in the resource group.")
except Exception as e:
    print(f"Error listing VMs: {e}")
