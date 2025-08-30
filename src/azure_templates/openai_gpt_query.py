import os

import openai  # Required for Azure OpenAI client
from icecream import ic

# Get Azure OpenAI credentials from environment variables
azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
api_key = os.environ.get("AZURE_OPENAI_API_KEY")

ic(azure_endpoint)
ic(api_key[:10] + "..." if api_key else None)  # Only show first 10 chars for security

if not api_key:
    print("Error: AZURE_OPENAI_API_KEY environment variable is not set")
    print("Please set it with: export AZURE_OPENAI_API_KEY=your_api_key")
    exit(1)

# Initialize the Azure OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version="2024-02-15-preview",  # Or your desired API version
)

resp = client.chat.completions.create(
    # Use the deployment name as shown in your project (or a serverless model name if you enabled it)
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Say hello from Azure in one sentence."}],
)
print(resp.choices[0].message.content)
