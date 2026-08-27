from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from config import API_KEY, BASE_URL, LLM_MODEL
from retrieval import get_retriever


llm = ChatOpenAI(
    model=LLM_MODEL,
    api_key=API_KEY,
    base_url=BASE_URL,
    temperature=0,
)


prompt = ChatPromptTemplate.from_template("""
You are Mohammad Hosein Salarali's personal AI assistant.

Answer the user's question using only the information provided
in the context below.

Rules:
- Do not invent or assume personal information.
- Do not use information outside the provided context.
- If the answer cannot be found in the context, say:
  "I don't have enough information in my knowledge base."
- Keep the answer clear and concise.

Context:
{context}

Question:
{question}

Answer:
""")


retriever = get_retriever(k=4)

def rag(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    messages = prompt.invoke({
        "context": context,
        "question": question,
    })

    response = llm.invoke(messages)

    sources = list({
        doc.metadata["source"]
        for doc in docs
    })

    return {
        "answer": response.content,
        "sources": sources,
    }

