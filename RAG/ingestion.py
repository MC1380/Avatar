from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import KNOWLEDGE_BASE_DIR


def load_documents() -> list[Document]:
    documents = []

    for file_path in KNOWLEDGE_BASE_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        document = Document(
            page_content=text,
            metadata={
                "source": file_path.name,
                "doc_type": file_path.stem.lower(),
            },
        )

        documents.append(document)

    return documents


def split_documents(
    documents: list[Document],
) -> list[Document]:

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    return text_splitter.split_documents(documents)