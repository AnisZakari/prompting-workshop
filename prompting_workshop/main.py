import argparse

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langsmith import traceable
from loguru import logger

from prompting_workshop.prompt_manager import Prompt
from prompting_workshop.vector_db import VectorDB

logger.level("INFO")

load_dotenv()
# MODEL = "gpt-4o-mini"
MODEL = "gpt-3.5-turbo"


@traceable
def rag_app(query: str) -> str:
    vector_db = VectorDB()
    prompt = Prompt()
    llm = ChatOpenAI(model=MODEL, temperature=0)

    documents = vector_db.query(query, top_k=4)
    documents_as_context = vector_db.documents_to_context(documents)
    logger.info(f"Documents as context: {documents_as_context}")
    prompt = prompt.populate(query, documents_as_context)
    response = llm.invoke(prompt)
    logger.debug(f"Response: {response}")
    return response, documents


@traceable
def rag_app_messages(messages: list[dict]) -> str:
    vector_db = VectorDB()
    llm = ChatOpenAI(model=MODEL, temperature=0)
    system, user = messages
    documents = vector_db.query(user.content, top_k=4)
    documents_as_context = vector_db.documents_to_context(documents)
    logger.info(f"Documents as context: {documents_as_context}")

    prompt = f"{system.content}\n\ncontext:\n{documents_as_context}\n\nquery:\n{user.content}"
    response = llm.invoke(prompt)
    logger.debug(f"Response: {response}")
    return response, documents


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    response, _ = rag_app(args.query)
    print(response)
