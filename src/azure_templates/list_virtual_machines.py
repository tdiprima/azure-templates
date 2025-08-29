# Script to list all Virtual Machines in a Resource Group.

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")

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
