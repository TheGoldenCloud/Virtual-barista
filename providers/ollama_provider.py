"""Chat preko lokalnog Ollama servera."""
import json
from functools import lru_cache

from ollama import Client

from config import MAX_TOOL_ROUNDS, OLLAMA_HOST, OLLAMA_MODEL
from prompts import SYSTEM_PROMPT
from tools import OLLAMA_TOOLS, run_tool
from utils import build_history


@lru_cache(maxsize=1)
def get_client():
    return Client(host=OLLAMA_HOST)


def _parse_tool_call(call):
    """Izvuci ime tool-a i argumente (radi i za Pydantic objekat i za dict)."""
    if hasattr(call, "function"):
        fn_name = call.function.name
        args = call.function.arguments
    else:
        fn_name = call["function"]["name"]
        args = call["function"]["arguments"]

    if isinstance(args, str):
        args = json.loads(args)
    return fn_name, args or {}


def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += build_history(history)
    messages.append({"role": "user", "content": message})

    for _ in range(MAX_TOOL_ROUNDS):
        response = get_client().chat(model=OLLAMA_MODEL, messages=messages, tools=OLLAMA_TOOLS)
        msg = response["message"]

        tool_calls = msg.get("tool_calls")
        print("DEBUG [ollama] tool_calls:", tool_calls)
        if not tool_calls:
            break

        messages.append(msg)
        for call in tool_calls:
            fn_name, args = _parse_tool_call(call)
            messages.append({"role": "tool", "content": run_tool(fn_name, args)})

    return msg.get("content") or ""
