# azure_openai_model_query.py
# Template for querying a deployed model in Azure OpenAI.

import os

from dotenv import load_dotenv
from icecream import ic
from openai import AzureOpenAI

load_dotenv()

# Variables (set these as environment variables)
# Where to get them:
# - AZURE_OPENAI_ENDPOINT: Azure Portal > Azure OpenAI > Your resource > Keys and Endpoint > Endpoint.
# - AZURE_OPENAI_API_KEY: Azure Portal > Azure OpenAI > Your resource > Keys and Endpoint > Key 1 or 2.
# - DEPLOYMENT_NAME: Azure AI Studio > Deployments > Your deployment (e.g., "gpt-4-deployment").
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")

ic(ENDPOINT)
ic(API_KEY[:10] + "..." if API_KEY else None)
ic(DEPLOYMENT_NAME)


def query_openai_model(prompt: str):
    # Initialize Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint=ENDPOINT, api_key=API_KEY, api_version="2024-02-15-preview"
    )

    # Query the model (chat completion example)
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7,
    )

    # Extract and print the response
    result = response.choices[0].message.content
    print(f"Model Response: {result}")

    return result


if __name__ == "__main__":
    user_prompt = "Explain what Azure OpenAI is in one sentence."
    query_openai_model(user_prompt)
