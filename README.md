# Azure Templates
Welcome to my plug-and-play template vault!

This collection comprises Python scripts designed to demonstrate basic Azure operations using the Azure SDK for Python. Each script is created as a reusable template, designed to function independently, annotated with comments for ease of understanding, and crafted following best practices.

- **Locating Variables in Azure**:
  - **Azure AI Studio Project**: Go to [Azure AI Studio](https://ai.azure.com/) > Select your project > In the project settings or deployments tab, find the **Project Name**, **Subscription ID**, **Resource Group**, and **Workspace Name** (for Azure ML integration). API keys/endpoints are under Deployments.
  - **Azure OpenAI**: In the Azure Portal > Search for "Azure OpenAI" > Select your resource > Go to "Keys and Endpoint" for **API Key**, **Endpoint URL**, and **Deployment Name** (e.g., for GPT models).
  - **Azure Machine Learning Workspace**: In Azure Portal > Search for "Machine Learning" > Select your workspace > Overview tab for **Workspace Name**, **Resource Group**, and **Subscription ID**.
  - **Azure AI Search**: In Azure Portal > Search for "Search services" > Select your service > "Keys" for **Admin Key** and **Endpoint**. Index names are under "Indexes" after creation.
  - **General**: Use Azure Portal > Your resource > "Access control (IAM)" to assign roles if needed (e.g., Contributor for ML workspaces).

These scripts cover essential Azure tasks and can be expanded by adding more parameters, error handling, or implementing asynchronous waits to enhance their functionality.

<br>
