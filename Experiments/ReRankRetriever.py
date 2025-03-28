from langchain_core.retrievers import BaseRetriever, RetrieverLike
from langchain_core.language_models import BaseLLM
from langchain_core.embeddings import Embeddings
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from typing import List
from sentence_transformers import SentenceTransformer


class ReRankRetriever(BaseRetriever):
    vectorstore : RetrieverLike

    model : SentenceTransformer

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun) -> List[Document]:

        docs = self.vectorstore.get_relevant_documents(query, k=10)
 
        queries = [query]
        sentences = []
        for i in docs:
            sentences.append(i.page_content)

        embeddings_1 = self.model.encode(sentences, normalize_embeddings=True)
        embeddings_2 = self.model.encode(queries, normalize_embeddings=True)
        similarity = embeddings_1 @ embeddings_2.T
        results = [(similarity[count][0], i) for count, i in enumerate(docs)]
        results = sorted(results, key=lambda x:x[0])

        return [i for _,i in results][0:4]