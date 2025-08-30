import os

from dotenv import load_dotenv
from icecream import ic
from openai import AzureOpenAI

load_dotenv()

# Load environment variables (set these in your environment or use a .env file)
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")  # Change to your deployment name, e.g., "gpt-4o"

ic(endpoint)
ic(api_key)
ic(deployment_name)

# Validate required variables
if not endpoint or not api_key:
    raise ValueError("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY environment variables.")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-01",
    # api_version="2024-02-01"  # Use a recent API version; check Azure docs for the latest
)

# Sample query to send to GPT-4
query_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of Japan?"}  # Replace with your own query
]

# Make the API call to query the model
response = client.chat.completions.create(
    model=deployment_name,  # This is the deployment name in Azure
    messages=query_messages,
    max_tokens=100,  # Adjust as needed
    temperature=0.7  # Adjust creativity level
)

# Print the response
print("GPT Response:")
print(response.choices[0].message.content.strip())

# Optional: Print usage details
print("\nUsage:")
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
print(f"Completion Tokens: {response.usage.completion_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
