# Retrieval-Augmented Generation (RAG) Systems Setup Guide

This README provides a comprehensive guide to setting up and running different Retrieval-Augmented Generation (RAG) systems. Each RAG system utilizes a distinct embedding model for retrieving information from a Chroma VectorDB before generating responses. Ensure to follow the setup steps carefully for the corresponding RAG system you wish to use.

## Prerequisites

Before proceeding with the setup for any of the RAG systems, ensure that you have the following prerequisites installed:

- Python 3.6 or higher
- Jupyter Notebook or JupyterLab
- Necessary Python packages as listed in `requirements.txt` (Install using `pip install -r requirements.txt`)

## RAG Systems Overview

The following RAG systems are available, each based on a different embedding model:

1. **RAG - GPT4All.ipynb**: Utilizes the GPT-4All embedding model for retrieval.
2. **RAG - LLM-Embedder.ipynb**: Based on the LLM-Embedder model for enhanced retrieval capabilities.
3. **RAG - Mistral_Llama7b.ipynb**: Employs the Mistral Llama7b embedding model.
4. **RAG - all-MiniLM-L6v2.ipynb**: Uses the all-MiniLM-L6v2 model for retrieval.

## General Setup Instructions

1. **Chroma VectorDB Creation**: Before running any RAG system, it's essential to create the appropriate Chroma VectorDB. This is done using the `Indexing/ChromaDBIndexer.ipynb` notebook. Follow the instructions within the notebook to create the VectorDB for your specific embedding model.

2. **Running a RAG System**: After setting up the VectorDB, you can proceed to run the desired RAG system. Open the corresponding `.ipynb` file in Jupyter Notebook or JupyterLab and execute the cells one by one. Ensure you've selected the correct kernel that meets the prerequisites.

### Specific Notes for Each RAG System

- **RAG - GPT4All**: Make sure the GPT4All VectorDB is correctly indexed as detailed in the ChromaDBIndexer notebook.

- **RAG - LLM-Embedder**: The LLM-Embedder requires a distinct setup within the VectorDB. Pay special attention to the embedding dimensions specified in the indexer.

- **RAG - Mistral_Llama7b**: Ensure that the Mistral_Llama7b VectorDB is correctly set up, considering the unique characteristics of this model.

- **RAG - all-MiniLM-L6v2**: This system requires the MiniLM-L6v2 VectorDB. Double-check the indexer settings to align with this model's requirements.

## Querying with LangChain

To invoke a query using LangChain in any of the RAG notebooks:

1. Navigate to the section titled 'RAG'.
2. Follow the specific instructions provided for configuring your query.
3. Be sure to have created an Agent and initailized the Llama generator model.
4. Execute the cells under this section to see the retrieved information and the generated response.

## Troubleshooting

- Ensure that all prerequisites are installed and updated to the required versions.
- Verify the VectorDB creation for each model was successful and without errors.
- For issues related to specific embedding models, refer to the respective model's documentation or support forums.
