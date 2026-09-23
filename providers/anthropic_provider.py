from functools import lru_cache

import anthropic

from config import ANTHROPIC_MODEL, MAX_TOKENS, MAX_TOOL_ROUNDS
from prompts import SYSTEM_PROMPT
from tools import ANTHROPIC_TOOLS, run_tool
from utils import build_history


@lru_cache(maxsize=1)
def get_client():
    return anthropic.Anthropic()


def chat(message, history):
    messages = build_history(history)
    messages.append({"role": "user", "content": message})

    for _ in range(MAX_TOOL_ROUNDS):
        response = get_client().messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=messages,
            tools=ANTHROPIC_TOOLS,
        )

        if response.stop_reason != "tool_use":
            break

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            print("DEBUG [anthropic] tool_use:", block.name, block.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": run_tool(block.name, block.input),
            })

        messages.append({"role": "user", "content": tool_results})

    return "".join(b.text for b in response.content if b.type == "text")
