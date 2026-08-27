# Projects

## LLM Projects

Repository: https://github.com/MC1380/LLM-Projects

This repository contains my projects and experiments related to Large Language Models, RAG, fine-tuning, chatbots, and AI applications.

---

### Restaurant AI Chatbot

* **Status:** Completed / Learning Project
* **Type:** LLM Application
* **Description:** An AI chatbot designed to work as a restaurant assistant.
* **Main Features:**

  * Conversational interaction with users
  * Access to restaurant item prices through tools
  * Interaction with a database
  * Providing information about the company and products
  * Showing images related to orders
* **Technologies:**

  * Python
  * LLM APIs
  * Database
  * Tool Calling
* **Main Concepts Learned:**

  * LLM-based chatbots
  * Tool usage
  * Database integration
  * AI application development

Repository path: `LLM-Projects/Chatbot`

---

### RAG Project

* **Status:** Completed / Learning Project
* **Type:** Retrieval-Augmented Generation
* **Description:** A RAG system that loads documents, splits them into chunks, converts them into embeddings, stores them in a vector database, retrieves relevant information, and uses an LLM to generate answers.
* **Main Components:**

  * Document loading
  * Document metadata
  * Text chunking
  * Embeddings
  * Vector database
  * Semantic retrieval
  * LLM generation
* **Technologies:**

  * Python
  * LangChain
  * Chroma
  * Hugging Face Embeddings
  * OpenAI-compatible APIs
  * Gradio
  * Scikit-learn
  * Plotly
* **Embedding Model:**

  * `all-MiniLM-L6-v2`
* **Text Splitter:**

  * `RecursiveCharacterTextSplitter`
  * Chunk size: 1000
  * Chunk overlap: 200
* **Vector Store:**

  * Chroma
* **Additional Work:**

  * Visualizing embeddings
  * Inspecting vector dimensions
  * Working with document metadata

The notebook loaded 76 documents and divided them into 413 chunks. The resulting embeddings had 384 dimensions.

Repository path: `LLM-Projects/RAG`

---

### Qwen Fine-tuning

* **Status:** Completed / Learning Project
* **Type:** LLM Fine-tuning
* **Model:**

  * Qwen3 4B
* **Description:** An experiment focused on fine-tuning a Qwen3 4B language model using a GPU-based environment.
* **Main Concepts:**

  * Model loading
  * Tokenization
  * Dataset preparation
  * Fine-tuning
  * Parameter-efficient fine-tuning
  * Quantization
  * LoRA / QLoRA
  * Model evaluation
* **Environment:**

  * Google Colab
  * NVIDIA T4 GPU
* **Technologies:**

  * Python
  * PyTorch
  * Transformers
  * Hugging Face
  * PEFT
  * BitsAndBytes

The notebook is a large Colab-based experiment and contains more than 10,000 lines of notebook content.

Repository path: `LLM-Projects/Fine tune`

---

### Meeting Minutes Creator

* **Status:** Completed / Learning Project
* **Type:** Speech-to-Text + LLM Application
* **Description:** An application for processing meeting recordings and creating meeting minutes using AI.
* **Main Components:**

  * Audio input
  * Speech processing
  * Automatic transcription
  * LLM-based text processing
  * Meeting minutes generation
* **Technologies:**

  * Python
  * Whisper / Speech Recognition
  * LLM
  * Gradio
* **Main Concepts Learned:**

  * Speech-to-text
  * Audio processing
  * Combining speech recognition with LLMs
  * Building AI applications

The project contains an `app.py` file together with audio resources and temporary processing files.

Repository path: `LLM-Projects/Meeting minutes creator`

---

### Website Summary

* **Status:** Completed / Learning Project
* **Type:** Web Scraping + LLM
* **Description:** A project for collecting information from websites and generating summaries using an LLM.
* **Main Components:**

  * Website scraping
  * Extracting website content
  * Processing extracted text
  * LLM-based summarization
* **Technologies:**

  * Python
  * Web Scraping
  * LLM
* **Main Files:**

  * `scraper.py`
  * `app.py`
  * `Website_Summary.ipynb`
* **Main Concepts Learned:**

  * Web scraping
  * Text extraction
  * LLM summarization
  * Building AI-powered applications

Repository path: `LLM-Projects/Website Summary project`

---

# Hugging Face Projects

Repository: https://github.com/MC1380/HugginFace

This repository contains experiments and projects focused on Hugging Face models, Transformers, speech recognition, text generation, and model quantization.

---

### Automatic Speech Recognition and Text Generation

* **Status:** Completed / Learning Project
* **Type:** Speech + LLM
* **Description:** An experiment combining automatic speech recognition with text generation using Hugging Face models.
* **Model:**

  * `Qwen/Qwen2.5-7B-Instruct`
* **Main Components:**

  * Audio input
  * Automatic Speech Recognition
  * Text generation
  * Hugging Face authentication
  * Model loading
* **Technologies:**

  * Python
  * PyTorch
  * Transformers
  * Hugging Face Hub
  * Google Colab
  * BitsAndBytes
* **Main Concepts Learned:**

  * ASR
  * Text generation
  * Transformer models
  * Hugging Face Hub
  * Model quantization
  * GPU-based inference

The notebook uses Transformers, `AutoTokenizer`, `AutoModelForCausalLM`, `BitsAndBytesConfig`, and a Qwen2.5 7B Instruct model.

Repository path: `HugginFace/Auto_Speech_Recognition_and_Text_Generation.ipynb`

---

### Hugging Face Project

* **Status:** Completed / Learning Project
* **Type:** Hugging Face Experiment
* **Description:** An experimental project for learning and working with Hugging Face models and tools.
* **Technologies:**

  * Python
  * Hugging Face
  * Transformers
* **Main Concepts:**

  * Loading pretrained models
  * Working with tokenizers
  * Model inference
  * Hugging Face ecosystem

Repository path: `HugginFace/HF_Project.ipynb`

---

### Quantization

* **Status:** Completed / Learning Project
* **Type:** LLM Optimization
* **Description:** An experiment focused on model quantization and reducing the memory requirements of large language models.
* **Main Concepts:**

  * Model quantization
  * Reduced-precision inference
  * Memory optimization
  * Efficient LLM deployment
* **Technologies:**

  * Python
  * PyTorch
  * Transformers
  * BitsAndBytes
  * Hugging Face

Repository path: `HugginFace/Quantization.ipynb`

---

### Python to C

* **Status:** Completed / Learning Project
* **Type:** Programming Experiment
* **Description:** An experiment related to translating or connecting Python code with C.
* **Main Concepts:**

  * Python
  * C
  * Programming language concepts
  * Code translation

Repository path: `HugginFace/Python_to_C.ipynb`

---

# Overall Project Experience

Through these projects, I have practiced and developed experience in:

* Python
* Large Language Models
* LLM APIs
* Hugging Face
* Transformers
* RAG
* Embeddings
* Vector Databases
* Chroma
* LangChain
* Fine-tuning
* LoRA
* QLoRA
* Quantization
* PyTorch
* Speech Recognition
* Text Generation
* Web Scraping
* LLM-based Summarization
* Chatbot Development
* Tool Calling
* Database Integration
* Gradio
* Google Colab
