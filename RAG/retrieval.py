from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from .config import (
    API_KEY,
    BASE_URL,
    CHROMA_DIR,
    EMBEDDING_MODEL,
)

from .ingestion import load_documents, split_documents


embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    api_key=API_KEY,
    base_url=BASE_URL,
)


def create_vectorstore():

    documents = load_documents()
    chunks = split_documents(documents)

    if CHROMA_DIR.exists():

        Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
            collection_name="personal_agent",
        ).delete_collection()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="personal_agent",
    )

    return vectorstore

def load_vectorstore():

    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name="personal_agent",
    )


def get_retriever(k: int = 4):

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )