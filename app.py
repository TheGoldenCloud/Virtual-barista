import gradio as gr

from config import DEFAULT_PROVIDER, PROVIDERS
from providers import PROVIDER_CHATS
from utils import to_text


def chat(message, history, provider=DEFAULT_PROVIDER):
    message = to_text(message)
    chat_fn = PROVIDER_CHATS.get(provider)
    if chat_fn is None:
        return f"Nepoznat provajder: {provider}"
    try:
        return chat_fn(message, history)
    except Exception as e:
        print(f"ERROR [{provider}]:", e)
        return f"Greska kod provajdera '{provider}': {e}"


def build_ui():
    return gr.ChatInterface(
        fn=chat,
        title="Virtual Barista",
        additional_inputs=[
            gr.Radio(choices=PROVIDERS, value=DEFAULT_PROVIDER, label="Model provider"),
        ],
    )


if __name__ == "__main__":
    build_ui().launch()
