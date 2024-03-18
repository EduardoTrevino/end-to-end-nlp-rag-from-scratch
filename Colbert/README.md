# Colbert RAG System Setup Guide

This README provides instructions for setting up and running the Colbert RAG (Retrieval-Augmented Generation) system using the `run_colbert_rag.ipynb` notebook. This system leverages a combination of the Colbert indexing system, a pre-trained model, and a language model for generating responses to queries.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or higher
- Access to Jupyter Notebook or JupyterLab
- An internet connection for downloading necessary files and packages

## Installation Steps

1. **Install Required Python Packages**:

    Install `ragatouille`, `gdown` for downloading files, and other necessary Python packages using pip:

    ```shell
    pip install ragatouille gdown
    pip install --upgrade --quiet langchain langchain-community langchainhub gpt4all chromadb
    pip install sentence-transformers
    ```

2. **Download Pre-trained Model**:

    Use the `gdown` tool to download the required pre-trained model files from a specified Google Drive folder.

    ```python
    import gdown
    gdown.download_folder("https://drive.google.com/drive/folders/1SqlQW2mtnkZk2rFwhhlN8mr1A7GL9z4Q?usp=sharing")
    ```

3. **Install Llama-Cpp-Python with Custom CMake Arguments**:

    Install `llama-cpp-python` package with specific CMake arguments to enable GPU acceleration:

    ```shell
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
    ```

4. **Download the LLaMA 2-7B Chat Model**:

    Download the LLaMA model using `wget`:

    ```shell
    wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q6_K.gguf
    ```

## Setting Up RAG Chain

1. **Initialize the RAGPretrainedModel**:

    Specify the path to your index and initialize the `RAGPretrainedModel`:

    ```python
    from ragatouille import RAGPretrainedModel

    path_to_index = "Ed/PretrainedColbertV2"
    RAG = RAGPretrainedModel.from_index(path_to_index)
    ```
    Or Upload innex to HF and from huggingface (This example is pulling a colbert fine-tune we made and available but not the one used in the report.)

    ```python
    from ragatouille import RAGPretrainedModel
    RAG = RAGPretrainedModel.from_pretrained(EddieT/colbert_cmu_lti_finetunev2.0)
    ```

3. **Set Up the LlamaCpp Language Model**:

    Configure `LlamaCpp` with your model path and desired settings.

4. **Create the RAG Chain Using LangChain**:

    Use `langchain` to create a retrieval and generation chain, customizing the prompt template as necessary for your application.

## Running the Notebook

- Execute the notebook cells sequentially to set up the environment, download the model, and configure the RAG chain.
- Load your list of questions from a file, adjusting the path to `FINALQUESTIONS.txt` as necessary.
- The system processes each question to generate and save answers in `colbert_out.txt`.

## Troubleshooting

- Ensure all required packages are installed and updated.
- If downloads fail, check your internet connection and the specified URLs.
- Verify the paths to the model and questions file are correct
