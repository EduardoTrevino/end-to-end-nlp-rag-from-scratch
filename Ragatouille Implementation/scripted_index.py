import numpy as np
import os
from ragatouille import RAGPretrainedModel

def main():
    RAG = RAGPretrainedModel.from_pretrained("EddieT/colbertv2.0_cmu_lti_finetunev1.0")
    base_dir = "../Data"
    folders = ["About Scottie", "Buggy News", "history_of_cmu", "history_of_scs", "Kiltie Band", "lti_faculty", "lti_programs", "Tartan Facts"]
    collection = []

    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt") and filename != "annotation.txt":
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    document_text = file.read()
                    collection.append(document_text)
    print(len(collection))

    for path in os.environ.get('PATH').split(os.pathsep):
        print(path)
    
    os.environ['COLBERT_LOAD_TORCH_EXTENSION_VERBOSE'] = 'True'
    os.environ['MKL_THREADING_LAYER'] = 'GNU'
    index_name = "colbertv2.0_cmu_lti_finetunev1.0"
    index_path = RAG.index(
        collection=collection,
        index_name=index_name,
        overwrite_index=True,
        max_document_length=180,
        split_documents=True,
    )

if __name__ == "__main__":
    main()