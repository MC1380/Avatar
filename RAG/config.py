import os
from pathlib import Path

from dotenv import load_dotenv


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge-base"
CHROMA_DIR = BASE_DIR / "chroma_db"

# Environment variables
load_dotenv(BASE_DIR / ".env")

# API
API_KEY = os.getenv("AVALAI_API_KEY")
BASE_URL = "https://api.avalai.ir/v1"

# Models
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1-nano"