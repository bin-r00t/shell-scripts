# Tokenizer

A command-line token counter using OpenAI's tiktoken library.

## Installation

```bash
# Install dependencies
uv sync
```

## Usage

### Basic Usage

```bash
# Pipe text to tokenizer
echo 'Hello, world!' | uv run tokenizer

# Count tokens in a file
cat file.txt | uv run tokenizer

# Multi-line text
cat << EOF | uv run tokenizer
This is a longer text
with multiple lines.
EOF
```

## How It Works

This tool uses tiktoken with the `cl100k_base` encoding, which is the same encoding used by GPT-4 and other modern OpenAI models. It reads text from stdin and outputs the token count to stdout.

## Examples

```bash
# English text
echo 'Hello, world!' | uv run tokenizer
# Output: 5

# Chinese text
echo '你好，世界！' | uv run tokenizer
# Output: 7

# From file
cat README.md | uv run tokenizer
# Output: 142
```

## Development

```bash
# Install development dependencies
uv sync

# Run the tool
uv run tokenizer

# Or run directly with Python
echo 'test' | python main.py
```
