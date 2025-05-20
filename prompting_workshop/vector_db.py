import random

from langchain.schema import Document
from langchain_community.retrievers import BM25Retriever
from langsmith import traceable

from prompting_workshop.utils import load_rag_data


class VectorDB:
    def __init__(self, data: list[Document] = None):
        self.data = data or [
            Document(page_content=item["answer"], metadata={"id": item["id"], "question": item["question"]})
            for item in load_rag_data()
        ]
        self.retriever = BM25Retriever.from_documents(self.data)

    @traceable
    def query(self, query: str, top_k: int = 3) -> list[str]:
        return self.retriever.get_relevant_documents(query=query, k=top_k)

    @traceable
    def documents_to_context(self, documents: list[Document]) -> str:
        return "\n\n".join(
            [f"ID: {d.metadata['id']}\nQuestion: {d.metadata['question']}\n: {d.page_content}" for d in documents]
        )

    def query_documents_as_context(self, query: str, top_k: int = 4) -> str:
        documents = self.query(query, top_k)
        return self.documents_to_context(documents)
