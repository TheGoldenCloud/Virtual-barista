def to_text(content):
    """Gradio ponekad salje content kao listu blokova [{'text':..,'type':'text'}]."""
    if isinstance(content, list):
        return " ".join(
            part.get("text", "") for part in content if isinstance(part, dict)
        )
    return content if content is not None else ""


def build_history(history):
    """Converts Gradio history (both formats) to a list of user/assistant messages."""
    messages = []
    for item in history:
        if isinstance(item, dict):                      
            if item.get("role") not in ("user", "assistant"):
                continue
            content = to_text(item.get("content"))
            if content:                                  
                messages.append({"role": item["role"], "content": content})
        else:                                            
            user_msg, assistant_msg = item
            if user_msg:
                messages.append({"role": "user", "content": to_text(user_msg)})
            if assistant_msg:
                messages.append({"role": "assistant", "content": to_text(assistant_msg)})
    return messages
