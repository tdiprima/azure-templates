"""
Simple Azure OpenAI GPT query example.

This script provides a minimal example of querying an Azure OpenAI GPT model
using API key authentication with environment variables for configuration.
"""

import os

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_version="2024-02-15-preview",  # use the latest your resource supports
)

resp = client.chat.completions.create(
    model=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello from Azure in one sentence."},
    ],
    temperature=0.2,
)
print(resp.choices[0].message.content)
