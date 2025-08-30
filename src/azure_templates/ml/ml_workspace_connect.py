# azure_ml_workspace_connect.py
# Template for connecting to an Azure ML workspace/project.

import os

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Variables (set these as environment variables or retrieve from Azure Key Vault)
# Where to get them:
# - SUBSCRIPTION_ID: Azure Portal > Subscriptions > Your subscription > Overview.
# - RESOURCE_GROUP: Azure Portal > Resource groups > Your group > Overview.
# - WORKSPACE_NAME: Azure Portal > Machine Learning > Your workspace > Overview.
SUBSCRIPTION_ID = os.environ.get("AZURE_SUBSCRIPTION_ID", "your-subscription-id")
RESOURCE_GROUP = os.environ.get("AZURE_RESOURCE_GROUP", "your-resource-group")
WORKSPACE_NAME = os.environ.get("AZURE_ML_WORKSPACE_NAME", "your-workspace-name")


def connect_to_ml_workspace():
    # Use DefaultAzureCredential for auth (logs in via Azure CLI or managed identity)
    credential = DefaultAzureCredential()

    # Connect to the workspace
    ml_client = MLClient(
        credential, subscription_id=SUBSCRIPTION_ID, resource_group_name=RESOURCE_GROUP
    )

    # Get the workspace object (this "connects" to the project)
    workspace = ml_client.workspaces.get(WORKSPACE_NAME)

    print(f"Connected to Azure ML Workspace: {workspace.name}")
    print(f"Location: {workspace.location}")
    print(f"Description: {workspace.description}")

    # Template usage: Now you can use ml_client to manage resources, e.g., ml_client.jobs.list()
    return ml_client


if __name__ == "__main__":
    connect_to_ml_workspace()
