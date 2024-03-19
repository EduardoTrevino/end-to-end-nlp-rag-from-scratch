# RAG Re-ranking System Setup Guide

This guide provides instructions for setting up and running the `run_rag_rereanking.ipynb` notebook. This system leverages a combination of vector stores, custom re-ranking, and language models for processing and generating responses to queries with an enhanced focus on relevance and accuracy.

## Prerequisites

Before you begin, ensure you have:

- Python 3.6 or higher
- Access to Jupyter Notebook or JupyterLab
- An internet connection for downloading necessary packages and models

## Installation Steps

1. **Install Required Python Packages**:

    Install necessary Python packages including `langchain`, `sentence_transformers`, and `llama-cpp-python`:

    ```shell
    pip install --upgrade --quiet langchain langchain-community langchainhub
    pip install sentence-transformers
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
    ```

2. **Model Setup**:

    The notebook utilizes the `BAAI/llm-embedder` and `BAAI/bge-reranker-base` models for embeddings and re-ranking, respectively. Ensure these models are correctly specified in the notebook.

## Notebook Overview

- **Vector Store Creation**: Initializes a `Chroma` vector store with embeddings from the `BAAI/llm-embedder` model.
- **Sentence Transformer Model**: Utilizes `SentenceTransformer` with the `BAAI/bge-reranker-base` model for re-ranking documents based on query similarity.
- **Custom Retriever**: Implements a custom retriever class that integrates the vector store and re-ranking model to retrieve and rank documents.
- **Language Model Setup**: Configures `LlamaCpp` as the language model for generating responses based on the re-ranked documents.
- **RAG Chain**: Constructs a RAG chain that processes queries, retrieves and re-ranks documents, and generates answers using the language model.

## Running the Notebook

- Execute the notebook cells sequentially to install dependencies, set up the models, and configure the custom retriever and RAG chain.
- Load your questions from `FINALQUESTIONS.txt` and adjust the path as necessary.
- The system processes each question to generate and save answers in `SubmissionData/system_outputs/graham_reranking.txt`.

## Troubleshooting

- Ensure all Python packages and dependencies are correctly installed.
- Verify that the model paths and names are correct and accessible.
- If encountering issues with the vector store or re-ranking, double-check the embeddings and model configurations.
