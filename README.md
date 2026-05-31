# FWFT ⚡ (Few Words Few Tokens)

A highly optimized system instruction and developer skill designed to enforce strict token efficiency, direct execution, and zero unnecessary verbosity for AI agents. 

---

## 🎯 Objective

Modern LLMs are often overly verbose, writing long explanations, greetings, and conversational filler that consumes valuable context window space and increases response latency. **FWFT** solves this by establishing strict guidelines that compel models to perform requested work immediately, outputting only what is directly necessary to satisfy the request.

---

## 📂 Repository Structure

```text
FWFT/
├── skill/
│   └── fwft-core/
│       └── SKILL.md      # Core guidelines and configuration for Gemini/Antigravity
├── .cursorrules          # Rules for Cursor AI integration
├── README.md             # Repository overview and documentation
└── LICENSE               # MIT License
```

---

## 🛠️ Usage & Integration

### ♊ Gemini / Antigravity IDE
#### Global Installation
To make the **FWFT** skill available across all your workspaces globally, copy the `fwft-core` directory into your global configuration folder:

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse -Force ".\skill\fwft-core" "$env:USERPROFILE\.gemini\config\skills\fwft-core"
```

**macOS / Linux:**
```bash
cp -r ./skill/fwft-core ~/.gemini/config/skills/fwft-core
```

#### Local Workspace Integration
Place the `skill/fwft-core` directory inside your project's active workspace or skills path and add it to your configuration: 

```json
{
  "skills": [
    "fwft-core"
  ]
}
```

---

### 🚀 Cursor
To enable FWFT behavior in Cursor:
1. Copy the `.cursorrules` file to the root of your project workspace.
2. Cursor will automatically detect and apply these rules to all chat, composer, and inline edit sessions.

---

### 🧡 Anthropic Claude
To enforce FWFT rules with Claude:
* **Claude Projects**: Copy the content of [SKILL.md](./skill/fwft-core/SKILL.md) and paste it directly into your project's **Custom Instructions**.
* **Claude Desktop**: Add the rules as system instructions in your `claude_desktop_config.json` system prompt properties or MCP server prompts.

---

### 💻 OpenAI Codex / API
To use FWFT with Codex or other OpenAI models:
* Pass the raw text of [SKILL.md](./skill/fwft-core/SKILL.md) as the **System Message** (or **Developer Message**) when making chat completions or configuring assistants in the OpenAI Playground.

---

## 📈 Contrast Comparison

### Verbose Mode (Standard LLM Response)
> "Sure! I can help you with creating that simple python function. Here is the implementation of a quick Fibonacci generator. I've designed it recursively for simplicity, though an iterative approach is faster for larger numbers. Let me know if you want me to write that version instead!"
> ```python
> def fibonacci(n):
>     if n <= 1:
>         return n
>     return fibonacci(n-1) + fibonacci(n-2)
> ```
> "I hope this code helps! Let me know if you have any other questions."

### FWFT Mode (⚡ Active)
> ```python
> def fibonacci(n):
>     if n <= 1:
>         return n
>     return fibonacci(n-1) + fibonacci(n-2)
> ```

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.
