# 🧠 AI Shell Helper

**AI Shell Helper** is a command-line assistant built in Python that brings the power of GPT-4 to your Linux terminal.

It explains shell commands, helps with Linux system tasks, and generates usable shell scripts — all from natural language, right in the terminal.

---

## ✨ Features

- `explain`: Break down complex shell commands in plain English  
- `howto`: Ask how to do something in Linux  
- `script`: Generate shell scripts from task descriptions  
- `chat`: REPL mode — talk to your terminal like a Linux-savvy AI

---

## 📁 Project Structure
---

## 🚀 Usage

Run any of the following from the project root:

```bash
python3 main.py explain "ls -la"
python3 main.py howto "mount a USB drive"
python3 main.py script "rename all .txt files to .md"
python3 main.py chat

MOCK_MODE=true
python3 main.py explain "ls -la"

[MOCK RESPONSE] You asked: Explain what this shell command does:
ls -la
---

## 📜 License

MIT License — see [LICENSE](./LICENSE)

