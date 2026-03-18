#!/bin/bash
# Build script to compile tokenizer with Nuitka

set -e

echo "Building tokenizer binary with Nuitka..."

python -m nuitka \
    --standalone \
    --onefile \
    --enable-plugin=tk-inter \
    --output-dir=dist \
    --output-filename=tokenizer \
    --remove-output \
    --follow-imports \
    --include-package=tiktoken \
    --include-package=dataclasses \
    main.py

echo "✓ Build complete! Binary available at: ./dist/tokenizer"
echo ""
echo "Usage:"
echo "  ./dist/tokenizer < file.txt"
echo "  cat file.txt | ./dist/tokenizer"
echo "  echo 'Hello' | ./dist/tokenizer"
