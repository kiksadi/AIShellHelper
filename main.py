#!/usr/bin/env python3

# AI Shell Helper
# Copyright (c) 2025 [Your Name]
# Licensed under the MIT License

import argparse
from ai_helper.core import explain_command, howto_task, script_task, chat_repl

def main():
    # Set up command-line parser
    parser = argparse.ArgumentParser(description="AI Shell Helper - Linux CLI Assistant")
    subparsers = parser.add_subparsers(dest="command")

    # 'explain' command
    explain_parser = subparsers.add_parser("explain", help="Explain a shell command")
    explain_parser.add_argument("input", help="Shell command to explain")

    # 'howto' command
    howto_parser = subparsers.add_parser("howto", help="Help with a Linux task")
    howto_parser.add_argument("task", help="Describe the task you want help with")

    # 'script' command
    script_parser = subparsers.add_parser("script", help="Generate a shell script for a task")
    script_parser.add_argument("task", help="Describe the task you want a script for")

    # 'chat' command
    chat_parser = subparsers.add_parser("chat", help="Interactive chat mode")

    # Parse and route command
    args = parser.parse_args()

    if args.command == "explain":
        explain_command(args.input)
    elif args.command == "howto":
        howto_task(args.task)
    elif args.command == "script":
        script_task(args.task)
    elif args.command == "chat":
        chat_repl()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

