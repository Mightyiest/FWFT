# FWFT ⚡ (Few Words Few Tokens)

A highly optimized system instruction and developer skill designed to enforce strict token efficiency, direct execution, and zero unnecessary verbosity for AI agents. 

---

## 🎯 Objective

Modern LLMs are often overly verbose, writing long explanations, greetings, and conversational filler that consumes valuable context window space and increases response latency. **FWFT** solves this by establishing strict guidelines that compel models to perform requested work immediately, outputting only what is directly necessary to satisfy the request.

---
## Screenshot

### Prompt

`Write a python script that fetches the current price of Bitcoin from a public API, handles rate limits, and saves it to a CSV file.`

<img width="1280" height="1114" alt="image" src="https://github.com/user-attachments/assets/dae29b87-81f4-4460-838a-7b4c2fc7b0e9" />



## 📂 Repository Structure

```text
FWFT/
├── skill/
│   └── fwft-core/
│       ├── fwft-core-compact.md            # Ultra-dense brevity rules for Gemini/Antigravity
│       └── fwft-pure-calculation-output.md # Pure Calculation Output (PCO) skill rules
├── .cursorrules          # Rules for Cursor AI integration
├── GEMINI.md             # Rules for Antigravity global instructions integration
├── README.md             # Repository overview and documentation
└── LICENSE               # MIT License
```

---

## 🛠️ Usage & Integration

### ♊ Gemini / Antigravity IDE
#### Global System Instructions (GEMINI.md)
To configure global default system instructions in **Antigravity IDE**:
1. Copy the [GEMINI.md](./GEMINI.md) file to your user profile directory:
   * **Windows (PowerShell):** `Copy-Item ".\GEMINI.md" "$env:USERPROFILE\.gemini\GEMINI.md"`
   * **macOS / Linux:** `cp ./GEMINI.md ~/.gemini/GEMINI.md`
2. Restart the IDE or initiate a new session to load these global instructions automatically.

#### Global Skill Installation
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
* **Claude Projects**: Copy the content of [fwft-core-compact.md](./skill/fwft-core/fwft-core-compact.md) and paste it directly into your project's **Custom Instructions**.
* **Claude Desktop**: Add the rules as system instructions in your `claude_desktop_config.json` system prompt properties or MCP server prompts.

---

### 💻 OpenAI Codex / API
To use FWFT with Codex or other OpenAI models:
* Pass the raw text of [fwft-core-compact.md](./skill/fwft-core/fwft-core-compact.md) as the **System Message** (or **Developer Message**) when making chat completions or configuring assistants in the OpenAI Playground.

---

## 🧮 Pure Calculation Output (PCO)

The **Pure Calculation Output (PCO)** skill forces the model to respond strictly with the final result of any mathematical, logical, or boolean calculation, suppressing all narrative and reasoning:

* **Internal Reasoning**: The model is configured to restrict all internal thinking/steps to calculations and numbers only, keeping the final output clean.
* **Word Problem Reduction**: Automatically parses word problems internally and returns only the calculated answer.
* **Ambiguous Requests**: If a request cannot be reduced to a computational problem, it returns `ERROR: Not a calculable request`.

Refer to [fwft-pure-calculation-output.md](./skill/fwft-core/fwft-pure-calculation-output.md) for full PCO instructions and examples.

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
