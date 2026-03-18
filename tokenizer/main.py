#!/usr/bin/env python3
"""A command-line token counter using tiktoken."""

import sys
import tiktoken


def main():
    """Read text from stdin and count tokens."""
    # Read all input from stdin
    text = sys.stdin.read()

    # If no input, show usage and exit
    if not text:
        sys.stderr.write("Usage: cat file.txt | tokenizer or echo 'text' | tokenizer\n")
        sys.exit(1)

    # Get encoding for the specified model (default to cl100k_base, used by GPT-4)
    encoding = tiktoken.get_encoding("cl100k_base")

    # Count tokens
    tokens = encoding.encode(text)
    token_count = len(tokens)

    # Output the count
    print(token_count)


if __name__ == "__main__":
    main()
