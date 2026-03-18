# shell-scripts

这个仓库用于收集一些日常使用的小工具/脚本。目前包含一个子项目：

- `tokenizer/`：基于 OpenAI 的 `tiktoken` 的命令行 token 计数器。支持从标准输入读取文本并输出 token 数量；可用 `uv` 运行，也可以通过脚本构建为独立二进制。

## 目录

- [tokenizer](./tokenizer)

## 快速开始

```bash
cd tokenizer
uv sync

echo 'Hello, world!' | uv run tokenizer
```

## License

各子目录可能包含各自的 LICENSE；请以对应目录下的 LICENSE 为准。