# Virtual Barista

Chatbot for cafe (Gradio) that works with Ollama or Anthropic model and receives orders via tool.

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