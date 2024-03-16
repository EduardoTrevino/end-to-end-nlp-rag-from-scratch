# end-to-end-nlp-rag-from-scratch
CMU Advanced NLP Assignment 2: End-to-end NLP System Building

## Setup instructions

Upload only 3 files to colab (or whatever setup you are using)

1. RAG.py
2. ReRankerRetriever.py
3. requirements.txt


## Example 

```python
pip install -r requirements.txt
python RAG.py --model_type rerank --vector_db llm_embed --rerank_model bge --test_set_path questions.txt --system_out_path rerank_system_out.txt
```

For more details on all the args run

```python
python RAG.py -h
```