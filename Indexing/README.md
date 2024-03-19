# ChromaDB and Colbert Indexers Setup Guide

This guide provides instructions for setting up and executing notebooks for creating various embeddings and indexes using ChromaDB and the Colbert model. These procedures are crucial for preparing your data for retrieval-augmented generation tasks.

## Prerequisites

Before proceeding, ensure you have:

- Python 3.6 or higher
- Access to Jupyter Notebook or JupyterLab
- An internet connection for downloading necessary packages and models

## Installation Steps

1. **Install Required Python Packages**:

    For all notebooks, you'll need to install specific Python packages. Execute the following commands at the beginning of each notebook:

    ```shell
    pip3 install --upgrade --quiet langchain langchain-community langchainhub gpt4all chromadb
    pip3 install sentence-transformers
    pip install ragatouille
    ```

    Additional steps for `ColbertV2VanillaIndexer.ipynb` include setting up ColBERT and its dependencies:

    ```shell
    !git -C ColBERT/ pull || git clone https://github.com/stanford-futuredata/ColBERT.git
    !pip install -U pip
    !pip install -e ColBERT/['faiss-gpu','torch']
    ```

2. **Prepare Your Data**:

    Ensure you have your dataset split and serialized in pickle format as `final_final.pkl`. This file should contain your dataset splits used across the notebooks.

## Notebooks Overview

### CChromaDBIndexer

- Creates vector databases using different embedding models.
- Supports GPT4All, all-MiniLM-L6-v2, LLM Embedder, and Mistral embeddings.
- Ensure you adjust the `createDB` function calls to match your dataset and desired embedding models.

### ColbertV2ClusterIndexer

- Demonstrates how to create clustered indexes using the ColbertV2 model.
- Utilizes pre-split data to create indexes for different groups or clusters.
- Modify the `groups` lists to represent your specific data clustering strategy.

### ColbertV2VanillaIndexer

- Guides through the process of creating a vanilla ColBERT index.
- Includes steps for installing ColBERT and its dependencies.
- Focuses on indexing a flat collection of documents without clustering.

## Running the Notebooks

Execute the Jupyter notebooks cell by cell, making sure to follow any specific instructions or notes within each notebook. Adjust the paths to your datasets or model files as necessary.

## Troubleshooting

- Ensure all Python packages and dependencies are correctly installed.
- Verify that your dataset files (`final_final.pkl`, `splitDocuments.pkl`) are correctly formatted and accessible.
- Check for any specific requirements or configurations noted within each notebook.
