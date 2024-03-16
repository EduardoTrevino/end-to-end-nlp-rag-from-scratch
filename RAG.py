


import argparse


stack_types = ["rerank", "zeroshot", "cluster", "hybrid"]
vector_dbs = ["llm_embed", "miniLM", "sfr_mistral", "gpt4", ""]
re_ranker = ["colbert", "bge"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_type",
        default=None,
        type=str,
        required=True,
        help="Model type selected in the list: " + ", ".join(stack_types),
    )

    parser.add_argument(
        "--vector_db",
        default=None,
        type=str,
        required=True,
        help="Vector database type selected in the list: " + ", ".join(vector_dbs),
    )

    parser.add_argument(
        "--rerank_model",
        default=None,
        type=str,
        required=False,
        help="Re-ranking models type selected in the list: " + ", ".join(re_ranker),
    )

    parser.add_argument(
        "--test_set_path",
        default=None,
        type=str,
        required=True,
        help="Path for test set .txt file",
    )

    parser.add_argument(
        "--system_out_path",
        default=None,
        type=str,
        required=True,
        help="Path for storing system generated outputs",
    )


    parser.add_argument(
        "--gpu",
        action="store_true",
        help="Whether or not to use CUDA"
    )

    args, unknown_args = parser.parse_known_args()

    model_type = args.model_type
    vector_db = args.vector_db
    rerank_model = args.rerank_model


    if model_type not in stack_types:
        raise ValueError("Unknown arguments detected: {}. Expected one of {}".format(model_type, stack_types))
    
    if vector_db not in vector_dbs:
        raise ValueError("Unknown arguments detected: {}. Expected one of {}".format(vector_db, vector_dbs))

    if (model_type == "hybrid" or  model_type == "rerank") and rerank_model == None:
        raise ValueError("Have chosen a hybrid or re-ranker RAG stack without without specifying on the re-ranking models: {}".format(re_ranker))
    
    if rerank_model != None and rerank_model not in re_ranker:
        raise ValueError("Unknown arguments detected: {}. Expected one of {}".format(rerank_model, re_ranker))









main()

