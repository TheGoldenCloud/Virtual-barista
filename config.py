import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")

PROVIDERS = ["anthropic", "ollama"]
DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "anthropic")

MAX_TOOL_ROUNDS = 5          
MAX_TOKENS = 1024            

OUTPUT_DIR = BASE_DIR / "output"
ORDERS_FILE = OUTPUT_DIR / "orders.txt"
