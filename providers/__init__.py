"""Registar provajdera: ime -> chat funkcija."""
from providers.anthropic_provider import chat as anthropic_chat
from providers.ollama_provider import chat as ollama_chat

PROVIDER_CHATS = {
    "anthropic": anthropic_chat,
    "ollama": ollama_chat,
}
