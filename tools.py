from config import ORDERS_FILE
from data.menu import mymenu
from datetime import datetime

# =====================================================================
#  Tool functions
# =====================================================================

def order_coffee_tool(coffee):
    print(f"Tool called to record coffee order: {coffee}")

    # Case-insensitive and space-insensitive comparison
    available = {item["name"].strip().lower(): item["name"] for item in mymenu}
    key = coffee.strip().lower()

    if key not in available:
        print("LLM returned coffee that we do not have")
        return (f"'{coffee}' is not on the menu. "
                f"Available: {', '.join(available.values())}")

    # Uzimanje trenutnog vremena i formatiranje
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ORDERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ORDERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Customer ordered: {available[key]}\n")

    return f"Order received at {timestamp}: {available[key]}"


# =====================================================================
#  Descriptions for the model (single source of truth) 
# =====================================================================

ORDER_COFFEE_SPEC = {
    "name": "order_coffee_tool",
    "description": (
        "Places an order for one coffee from the menu. Call it once the customer has "
        "clearly decided on a specific drink. Call it once per coffee if they order several."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "coffee": {
                "type": "string",
                "enum": [item["name"] for item in mymenu],
                "description": "Exact name of the coffee from the menu",
            }
        },
        "required": ["coffee"],
        "additionalProperties": False,
    },
}

# here you add new tools: spec in TOOL_SPECS, function in AVAILABLE_TOOLS
TOOL_SPECS = [ORDER_COFFEE_SPEC]
AVAILABLE_TOOLS = {
    "order_coffee_tool": order_coffee_tool,
}

# =====================================================================
#  Format conversion
# =====================================================================

# Ollama: {"type": "function", "function": {name, description, parameters}}
OLLAMA_TOOLS = [{"type": "function", "function": spec} for spec in TOOL_SPECS]

ANTHROPIC_TOOLS = [
    {
        "name": spec["name"],
        "description": spec["description"],
        "input_schema": spec["parameters"],
    }
    for spec in TOOL_SPECS
]


def run_tool(fn_name, args):
    """Executes the tool by name and always returns a string (even when an error occurs)."""
    fn = AVAILABLE_TOOLS.get(fn_name)
    if not fn:
        return f"Unknown tool: {fn_name}"
    try:
        return str(fn(**args))
    except Exception as e:
        return f"Tool error: {e}"
