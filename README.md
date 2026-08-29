# 🤖 Avatar — Mohammad's AI Agent

> A friendly AI assistant that knows about Mohammad, answers questions about him, and can help users get in touch with him.

**Avatar** is a personal AI Agent built to represent me as an interactive digital assistant.

Instead of simply providing static information, Avatar can understand a user's request, retrieve relevant information from my personal knowledge base, and use tools when an action is required.

---

## ✨ Features

* 💬 Natural-language conversation
* 🧠 Personal Knowledge Base with RAG
* 🔎 Semantic search using OpenAI Embeddings
* 🗃️ Chroma vector database
* 🤖 LLM-powered Agent
* 🛠️ Tool calling
* 📩 Contact request handling
* 🔔 Notification through ntfy
* 🌐 FastAPI backend
* 🎨 Gradio user interface
* 🔊 Welcome audio message
* 🌍 Persian & English conversation support

---

## 🧠 What Can Avatar Do?

### 1. Answer Questions About Me

Avatar has access to a personal Knowledge Base containing information about:

* Education
* Programming skills
* AI & Machine Learning
* LLMs
* Agentic AI
* Projects
* Interests

For example:

> **User:** What did Mohammad study at university?

Avatar retrieves the relevant information from the Knowledge Base and generates an answer.

---

### 2. Retrieval-Augmented Generation (RAG)

Instead of relying only on the LLM's knowledge, Avatar retrieves relevant information from my personal documents before generating an answer.

The retrieval pipeline is:

```text
User Question
      ↓
OpenAI Embedding
      ↓
Vector Search
      ↓
Chroma
      ↓
Relevant Documents
      ↓
LLM
      ↓
Answer
```

This allows Avatar to answer questions based on **my actual information** rather than guessing.

---

### 3. Tool Calling

Avatar can also use tools when a conversation requires an action.

Currently, Avatar has a contact tool that allows users to send a message to me.

For example:

> **User:** I want to get in touch with Mohammad.

Avatar collects:

* Name
* Email
* Message

and sends the contact request through a notification service.

```text
User
 ↓
Avatar Agent
 ↓
Contact Tool
 ↓
ntfy
 ↓
📱 Notification
```

---

## 🏗️ Architecture

The current architecture is intentionally simple:

```text
                         ┌──────────────┐
                         │     User     │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │    Gradio    │
                         │      UI      │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   FastAPI    │
                         │    Backend   │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │     Agent    │
                         └──────┬───────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
             ┌─────────────┐         ┌─────────────┐
             │     RAG     │         │    Tools    │
             └──────┬──────┘         └──────┬──────┘
                    │                       │
                    ▼                       ▼
                Chroma                  ntfy
                    │
                    ▼
            OpenAI Embeddings
                    │
                    ▼
                   LLM
```

---

## 📁 Project Structure

```text
Avatar/
│
├── Agent/
│   ├── agent.py
│   ├── tools.py
│   └── ...
│
├── RAG/
│   ├── ingestion.py
│   ├── retrieval.py
│   ├── rag.py
│   └── Test_RAG.ipynb
│
├── knowledge-base/
│   └── ...
│
├── chroma_db/
│   └── ...
│
├── assets/
│   ├── avatar.png
│   └── welcome.mp3
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI / LLM

* OpenAI API
* LangChain
* LangChain OpenAI
* Hugging Face ecosystem

### RAG

* OpenAI Embeddings
* Chroma
* Vector Search
* Document Chunking

### Agent

* LangChain
* Tool Calling
* LLM-based decision making

### Frontend

* Gradio

### Notifications

* ntfy

### Environment & Dependency Management

* `uv`
* `uv.lock`
* `.env`

### Deployment

* Render

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/MC1380/Avatar.git
cd Avatar
```

### 2. Install dependencies

This project uses [`uv`](https://docs.astral.sh/uv/).

If you have `uv` installed:

```bash
uv sync
```

This automatically creates/uses the virtual environment and installs the dependencies defined in `pyproject.toml` and `uv.lock`.

---

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
AVALAI_API_KEY=your_avalai_api_key
NTFY_TOPIC=your_ntfy_topic
```

> Never commit your `.env` file or expose API keys publicly.

---

### 4. Run the application

```bash
uv run uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### API Documentation

FastAPI automatically provides interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Avatar UI

The Gradio interface is available at:

```text
http://127.0.0.1:8000/app
```

---

## 🔄 How a User Request Works

A typical request goes through the following process:

```text
User
 ↓
Gradio
 ↓
FastAPI
 ↓
Agent
 ↓
Does the question require personal information?
 ├── No → Generate Answer
 │
 └── Yes
       ↓
      RAG
       ↓
   Vector Search
       ↓
    Retrieved Context
       ↓
       LLM
       ↓
     Answer
```

If the user wants to contact Mohammad:

```text
User
 ↓
Agent
 ↓
Collect Name + Email + Message
 ↓
Contact Tool
 ↓
ntfy
 ↓
Notification
```

---

## 🎯 Design Goals

Avatar was designed with a few simple goals:

### Keep it simple

The project intentionally avoids unnecessary complexity.

There is no complicated multi-agent architecture or state-management system. The goal is to build a practical and understandable AI Agent.

### Ground answers in real information

The Agent should use the Knowledge Base when answering questions about me instead of relying on the LLM's assumptions.

### Make the Agent useful

Avatar is not only a chatbot.

It can also use tools to perform actions, such as sending contact requests.

### Build while learning

Avatar is also a learning project where I applied concepts from:

* LLM Applications
* RAG
* Embeddings
* Vector Databases
* Agentic AI
* Tool Calling
* FastAPI
* Gradio
* Deployment

---

## 📚 What I Learned

Building Avatar helped me practice the complete lifecycle of an AI application:

```text
Knowledge Base
      ↓
Document Processing
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Retrieval
      ↓
RAG
      ↓
Agent
      ↓
Tool Calling
      ↓
FastAPI
      ↓
Gradio
      ↓
Deployment
```

The main lesson was that building an AI Agent is not just about calling an LLM.

The surrounding engineering — retrieval, tools, APIs, application structure, dependency management, and deployment — is equally important.

---

## 🌐 Live Demo

🚀 **Avatar is deployed and available online.**

[Open Avatar]([https://avatar-ai-xxxx.onrender.com](https://avatar-ai-mjf7.onrender.com/app/))

> Replace the URL above with the actual Render URL of the deployed application.

---

## 🔮 Future Improvements

Some ideas for future versions:

* 💾 Persistent conversation history
* 👤 Per-user sessions
* 📊 RAG evaluation dataset
* 📈 Retrieval & answer evaluation metrics
* 🧠 Improved retrieval and reranking
* 🔐 Better authentication and security
* 🎙️ Voice input
* 🔊 Voice responses
* 🗂️ More personal knowledge sources
* ⚡ Streaming responses
* 🧪 Automated testing
* 📦 Better production architecture

---

## 👨‍💻 About Me

I'm **Mohammad**, an Electrical Engineering graduate who is currently focused on becoming an **AI / ML Engineer**.

My current interests include:

* Python
* Machine Learning
* Deep Learning
* LLMs
* RAG
* Agentic AI
* AI Engineering

I built Avatar as a small step toward building more practical AI systems.

---

## ⭐ If You Find This Project Interesting

Feel free to explore the code, experiment with the architecture, and check out my other AI projects.

Thanks for visiting **Avatar** 🤖
