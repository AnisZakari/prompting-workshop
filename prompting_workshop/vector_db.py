import random

from langsmith import traceable

from prompting_workshop.utils import load_rag_data


class VectorDB:
    def __init__(self, data: list[str] = None):
        self.data = data or load_rag_data()

    @traceable
    def query(self, query: str, top_k: int = 4) -> list[str]:
        return random.sample(self.data, top_k)

    @traceable
    def documents_to_context(self, documents: list[str]) -> str:
        return "\n".join(documents)

    def query_documents_as_context(self, query: str, top_k: int = 4) -> str:
        documents = self.query(query, top_k)
        return self.documents_to_context(documents)
