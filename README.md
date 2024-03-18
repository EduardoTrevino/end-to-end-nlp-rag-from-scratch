# end-to-end-nlp-rag-from-scratch
CMU Advanced NLP Assignment 2: End-to-end NLP System Building

## Setup instructions
Most files were run in colab or locally (a mix). So the dependencies may be scattered. Most ipynb notebooks should have them. We have requirements.txt file, however this is not comrehensive. 

The notebooks usually contain 
- path to index
- path to input file
- path to output file

These need to be modified in order to run the notebooks


## Directory Structure
- Scraping: Holds code for pulling data from web
- Data: Holds our scraped data (moved from the scraping directory) 
- Indexing: Creates vectordbs and indexes for colbert
- Submission Data: Holds our train/test splits and system outputs from experiments
- Baseline Rag: Holds all our traditional rag systems with different embedding models used to create the retriever
- Reranking: Holds code for reranking with llm-embed vectordb and bge-large reranking model
- Colbert: Holds code for generating answers via colbert
- Cluster RAG: Holds code for cluster rag and unlimiformer
- Experiments: Holds code that we experimented with, not for submission or running

Evaluation.ipynb holds reproducible evaluation metrics from system outputs.

## Link to our vectordbs
Our vectordbs and indexes are stored in this gdrive

https://drive.google.com/drive/folders/1w76-AicyVWk_ukVOcM_M8es4eQdaVx-s?usp=drive_link
