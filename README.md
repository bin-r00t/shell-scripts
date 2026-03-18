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

## Building Standalone Binary

You can compile the project into a standalone binary that doesn't require Python environment:

```bash
# Build the binary (takes a few minutes)
uv run bash build.sh

# The binary will be created at ./dist/tokenizer (~34MB)

# Install system-wide (optional)
mkdir -p ~/.local/bin
cp dist/tokenizer ~/.local/bin/

# Add to PATH if not already there (for zsh)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

After installation, you can use `tokenizer` directly from anywhere:

```bash
echo 'Hello, world!' | tokenizer
cat file.txt | tokenizer
```

The build process uses [Nuitka](https://nuitka.net/) to compile Python code into C++, then into a native binary. All dependencies (including Python runtime and tiktoken) are bundled into a single executable file.