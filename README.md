# Virtual Barista

Small AI agent that sells coffee: a virtual barista chatbot that recommends drinks from the menu and places orders through tool calling. Runs on a local Ollama model or on Claude via the Anthropic API, switchable in the Gradio UI.

## Structure

```
barista-chatbot/
├── app.py # entry point: Gradio UI + provider selection
├── config.py # settings (cita .env)
├── prompts.py # system prompt
├── tools.py # tools: functions, descriptions, format conversion
├── utils.py # to_text, build_history
├── providers/
│ ├── __init__.py # provider registry
│ ├── anthropic_provider.py
│ └── ollama_provider.py
├── date/
│ ├── menu.py # mymenu
│ └── details.py # mydetails
├── output/ # orders.txt (generated)
├── .env.example
├── .gitignore
└── requirements.txt
```

## Starting

```bash
python -m venv .venv
.venv\Scripts\activate.bat #For CMD or .\.venv\Scripts\Activate.ps1 for Powershell
pip install -r requirements.txt
cp .env.example .env # then enter your ANTHROPIC_API_KEY
python app.py
```