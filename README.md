# AIShellHelper
chatGPT in you Linux shell

What is AI Shell Helper?
AI Shell Helper is a command-line assistant written in Python that brings the power of GPT-4 (via OpenAI's API) to the Linux terminal.

It helps users:

🔍 Understand shell commands (what does awk or tar -czvf really do?)

🛠️ Figure out how to do Linux tasks (like mounting drives or renaming files)

📜 Generate shell scripts from plain English descriptions

💬 Chat in REPL mode like a smart terminal buddy

🌟 Why it was built:
“I wanted a smarter, faster way to solve terminal problems without switching between windows or digging through Stack Overflow. This project started as a personal assistant and grew into something educational and time-saving.”

ai-shell-helper/
├── ai_helper/             # Core logic and API integration
│   └── core.py
├── tests/                 # Unit tests for core functionality
│   └── test_core.py
├── main.py                # CLI entry point
├── requirements.txt       # Python dependencies
├── setup.py               # (Optional) For installing as a package
├── .env                   # Your API key (not pushed to GitHub)
├── .gitignore             # Files Git should ignore
└── README.md              # Project overview and usage
