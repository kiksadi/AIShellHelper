# AI Shell Helper - Core Functions
# Copyright (c) 2025 [Your Name]
# Licensed under the MIT License

import os
import openai
from dotenv import load_dotenv

# Load OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🔎 Calls OpenAI with a prompt and returns the response
def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful Linux shell expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.5
    )
    return response['choices'][0]['message']['content']

# 🧠 Explain a shell command
def explain_command(command):
    prompt = f"Explain what this shell command does:\n\n{command}"
    print(call_openai(prompt))

# 🔧 Help with how to do a Linux task
def howto_task(task):
    prompt = f"How do I do this task in Linux?\n\n{task}"
    print(call_openai(prompt))

# 📜 Generate a shell script
def script_task(task):
    prompt = f"Write a shell script to accomplish the following task:\n\n{task}"
    print(call_openai(prompt))

# 💬 Interactive chat mode (REPL)
def chat_repl():
    print("🤖 AI Shell Helper - Chat Mode (type 'exit' to quit)")
    while True:
        try:
            user_input = input("> ")
            if user_input.strip().lower() in ["exit", "quit"]:
                print("👋 Bye!")
                break
            print(call_openai(user_input))
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Bye!")
            break

