# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A simple CLI tool that counts tokens using OpenAI's `tiktoken` library with `cl100k_base` encoding (GPT-4 compatible). The tool reads text from stdin and outputs the token count to stdout.

## Architecture

Single-file Python project (`main.py`) with minimal dependencies:
- `tiktoken>=0.8.0` - OpenAI's token encoding library
- Uses `cl100k_base` encoding (standard for GPT-4 and modern OpenAI models)
- Reads from stdin, writes to stdout, errors to stderr

The entry point is configured in `pyproject.toml` as `[project.scripts]` pointing to `main:main`.

## Common Commands

### Development

```bash
# Install dependencies
uv sync

# Run the tool (requires uv)
echo 'text' | uv run tokenizer

# Run directly with Python
echo 'text' | python main.py
```

### Building Standalone Binary

The project uses Nuitka to compile a standalone binary (~34MB) that doesn't require Python:

```bash
# Build the binary
uv run bash build.sh

# The binary is created at ./dist/tokenizer
# Can be installed system-wide:
mkdir -p ~/.local/bin && cp dist/tokenizer ~/.local/bin/
```

The `build.sh` script uses these Nuitka flags:
- `--standalone --onefile` - Creates single executable with bundled dependencies
- `--include-package=tiktoken` - Ensures tiktoken is included
- `--output-dir=dist --output-filename=tokenizer` - Output configuration

## Testing

```bash
# Basic functionality test
echo 'Hello, world!' | uv run tokenizer  # Expected: 5

# Chinese text test
echo '你好，世界！' | uv run tokenizer  # Expected: 7

# File input
cat README.md | uv run tokenizer
```

## Encoding Details

Uses `tiktoken.get_encoding("cl100k_base")` which handles:
- English text efficiently
- Multi-byte characters (Chinese, emojis, etc.)
- Compatible with GPT-4, GPT-3.5-turbo, and modern OpenAI models
