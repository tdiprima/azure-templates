import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",  # Check Azure docs for the latest
)

# Sample query to send to GPT-4
query_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "What is the capital of Japan?",
    },
]

# Make the API call to query the model
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=query_messages,
    max_tokens=100,  # Adjust as needed
    temperature=0.7,  # Adjust creativity level
)

# Print the response
print("GPT Response:")
print(response.choices[0].message.content.strip())

# Optional: Print usage details
print("\nUsage:")
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
print(f"Completion Tokens: {response.usage.completion_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
