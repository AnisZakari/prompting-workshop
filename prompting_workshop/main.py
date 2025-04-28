import argparse

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langsmith import traceable

from prompting_workshop.prompt_manager import Prompt
from prompting_workshop.vector_db import VectorDB

load_dotenv()


@traceable
def rag_app(query: str) -> str:
    vector_db = VectorDB()
    prompt = Prompt()
    llm = ChatOpenAI()

    documents_as_context = vector_db.query_documents_as_context(query, top_k=5)
    prompt = prompt.populate(query, documents_as_context)
    response = llm.invoke(prompt)

    return response


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    response = rag_app(args.query)
    print(response)
