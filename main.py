from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr

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


def gradio_chat(message, history):

    if not message.strip():
        return "", history

    response = run_agent(message)

    history.append({
        "role": "user",
        "content": message,
    })

    history.append({
        "role": "assistant",
        "content": response,
    })

    return "", history


with gr.Blocks(
    title="Avatar - AI Assistant"
) as demo:

    gr.Markdown(
        """
        # 🤖 Avatar

        ### Your friendly AI assistant for Mohammad

        Ask me anything about Mohammad, his skills,
        projects, education, or interests.
        """
    )

    with gr.Row():

        with gr.Column(scale=1):

            gr.Image(
                value="assets/avatar.png",
                show_label=False,
                interactive=False,
            )

            gr.Markdown(
                """
                ### 👋 Welcome

                Listen to my welcome message before you start chatting!
                """
            )

            gr.Audio(
                value="assets/welcome.mp3",
                autoplay=False,
                show_label=False,
            )

        with gr.Column(scale=2):

            chatbot = gr.Chatbot(
                label="Chat with Avatar",
                height=500,
            )

            with gr.Row():

                message = gr.Textbox(
                    placeholder="Ask Avatar something...",
                    label="Message",
                    scale=4,
                )

                send = gr.Button(
                    "Send 🚀",
                    scale=1,
                )

            clear = gr.Button(
                "Clear Chat",
            )

    send.click(
        gradio_chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot],
    )

    message.submit(
        gradio_chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot],
    )

    clear.click(
        lambda: [],
        outputs=chatbot,
    )


app = gr.mount_gradio_app(
    app,
    demo,
    path="/app",
)