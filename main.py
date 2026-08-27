from fastapi import FastAPI
from pydantic import BaseModel

from Agent.agent import run_agent


app = FastAPI(
    title="Avatar API",
    description="AI assistant for Mohammad",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "message": "Avatar API is running 🚀"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = run_agent(request.message)

    return ChatResponse(
        response=response
    )