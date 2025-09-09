"""
Simple Azure OpenAI GPT query example.

This script provides a minimal example of querying an Azure OpenAI GPT model
using API key authentication with environment variables for configuration.
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview",  # use the latest your resource supports
)

resp = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello from Azure in one sentence."},
    ],
    temperature=0.2,
)
print(resp.choices[0].message.content)
