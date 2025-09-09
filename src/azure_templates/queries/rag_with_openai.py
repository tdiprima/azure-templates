# azure_rag_with_openai.py
# Template for RAG using Azure OpenAI (for generation) and Azure AI Search (for retrieval).

import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv
from icecream import ic
from openai import AzureOpenAI

load_dotenv()

# Variables (set these as environment variables)
# Where to get them:
# - AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, DEPLOYMENT_NAME: Same as in azure_openai_model_query.py.
# - SEARCH_ENDPOINT: Azure Portal > Search services > Your service > Overview > URL.
# - SEARCH_API_KEY: Azure Portal > Search services > Your service > Keys > Primary admin key.
# - SEARCH_INDEX_NAME: Azure Portal > Search services > Your service > Indexes > Your index name (create one with vector fields if needed).
# - EMBEDDING_DEPLOYMENT: Azure AI Studio > Deployments > Your embedding model deployment (e.g., "text-embedding-ada-002").
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "https://your-endpoint.openai.azure.com/")
OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "your-api-key")
OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "your-gpt-deployment")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "your-embedding-deployment")
SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT", "https://your-search-service.search.windows.net")
SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY", "your-search-key")
SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME", "your-index-name")

masked_openai_api_key = f"{OPENAI_API_KEY[:10]}..." if OPENAI_API_KEY else None
masked_search_api_key = f"{SEARCH_API_KEY[:10]}..." if SEARCH_API_KEY else None

ic(OPENAI_ENDPOINT)
ic(masked_openai_api_key)
# ic(OPENAI_API_KEY and f"{OPENAI_API_KEY[:10]}...")
ic(OPENAI_DEPLOYMENT)
ic(EMBEDDING_DEPLOYMENT)
ic(SEARCH_ENDPOINT)
ic(masked_search_api_key)
ic(SEARCH_INDEX_NAME)


def generate_embeddings(text: str, client: AzureOpenAI):
    """Generate vector embeddings for the query using Azure OpenAI."""
    response = client.embeddings.create(model=EMBEDDING_DEPLOYMENT, input=text)
    return response.data[0].embedding


def perform_rag_query(user_query: str):
    # Initialize clients
    openai_client = AzureOpenAI(
        azure_endpoint=OPENAI_ENDPOINT, 
        api_key=OPENAI_API_KEY, 
        api_version="2024-02-01"
    )

    search_client = SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=SEARCH_INDEX_NAME,
        credential=AzureKeyCredential(SEARCH_API_KEY),
    )

    # Step 1: Embed the user query
    query_embedding = generate_embeddings(user_query, openai_client)

    # Step 2: Retrieve relevant documents via vector search
    vector_query = VectorizedQuery(
        vector=query_embedding, k_nearest_neighbors=3, fields="contentVector"
    )  # Assumes your index has a 'contentVector' field
    search_results = search_client.search(
        search_text=None,  # Pure vector search
        vector_queries=[vector_query],
        select=["id", "content"],  # Adjust fields based on your index schema
    )

    # Collect context from results
    context = "\n".join([result["content"] for result in search_results])

    # Step 3: Augment and query the model with RAG
    prompt = (f"Context: {context}\n\nQuestion: {user_query}\nAnswer based on the context:")
    response = openai_client.chat.completions.create(
        model=OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5,
    )

    result = response.choices[0].message.content
    print(f"RAG Response: {result}")

    return result


if __name__ == "__main__":
    # Assume your search index has relevant data
    query = ("What is the capital of Japan?")
    perform_rag_query(query)
