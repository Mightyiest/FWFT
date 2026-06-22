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

## Antigravity Prompt Comparison

| Feature | With Skill | Without Skill |
|----------|-----------|--------------|
| Screenshot | <img height="300" alt="With Skill" src="https://github.com/user-attachments/assets/cb584a51-68b3-4644-93fa-f5e7542dae2d" /> | <img height="300" alt="Without Skill" src="https://github.com/user-attachments/assets/cfee6687-d3ea-4f47-9b0a-f3265098f236" /> |
| Configuration | Antigravity + Skill | Antigravity Only |
| Purpose | Enhanced capability through skill injection | Baseline Antigravity prompt behavior |





## 📂 Repository Structure

```text
FWFT/
├── skill/
│   └── fwft-core/
│       └── SKILL.md                  # Unified core and calculation rules for Gemini/Antigravity
├── .cursorrules          # Rules for Cursor AI integration
├── GEMINI.md             # Rules for Antigravity global instructions integration
├── skill_router.py       # Dynamic skill routing engine for custom agent applications
├── README.md             # Repository overview and documentation
└── LICENSE               # MIT License
```

---

## 🛠️ Usage & Integration

### ♊ Gemini / Antigravity IDE

To maximize token efficiency and minimize prompt latency, use **Targeted Workspace Loading** (Recommended) rather than installing skills globally.

#### 1. Targeted Workspace Loading (Recommended)
Place the `skill/fwft-core` directory inside your active project's workspace:
```text
your-project-root/
└── skill/
    └── fwft-core/
        └── SKILL.md
```

Then add `fwft-core` to your active workspace configuration:
```json
{
  "skills": [
    "fwft-core"
  ]
}
```

#### 2. Global System Instructions (GEMINI.md)
To configure default system instructions globally across all workspaces:
1. Copy the [GEMINI.md](./GEMINI.md) file to your user profile directory:
   * **Windows (PowerShell):** `Copy-Item ".\GEMINI.md" "$env:USERPROFILE\.gemini\GEMINI.md"`
   * **macOS / Linux:** `cp ./GEMINI.md ~/.gemini/GEMINI.md`
2. Restart the IDE or initiate a new session to load these global instructions automatically.

#### 3. Alternative: Global Skill Installation (Not Recommended for Token Efficiency)
If you require `fwft-core` to be active across all workspaces globally without copying it to each project:

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse -Force ".\skill\fwft-core" "$env:USERPROFILE\.gemini\config\skills\fwft-core"
```

**macOS / Linux:**
```bash
cp -r ./skill/fwft-core ~/.gemini/config/skills/fwft-core
```

#### Token Optimization Strategy
* **Context Caching (Automatic)**: Antigravity automatically leverages Gemini's native Context Caching. When you load a large skill or system prompt, it is sent fully on the first request. On all subsequent requests in the same conversation, the static prompt tokens are cached. This eliminates the latency and reduces the cost of those tokens by up to 75%.
* **Targeted Workspace Loading**: Do not install skills globally in `.gemini/config/skills`. Keep the global configuration empty. Instead, place skills only in the local workspace directory where they are required, ensuring they are never loaded for irrelevant projects.

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

## 🧮 Pure Calculation Output (PCO)

The **Pure Calculation Output (PCO)** skill forces the model to respond strictly with the final result of any mathematical, logical, or boolean calculation, suppressing all narrative and reasoning:

* **Internal Reasoning**: The model is configured to restrict all internal thinking/steps to calculations and numbers only, keeping the final output clean.
* **Word Problem Reduction**: Automatically parses word problems internally and returns only the calculated answer.
* **Ambiguous Requests**: If a request cannot be reduced to a computational problem, it returns `ERROR: Not a calculable request`.

Refer to [SKILL.md](./skill/fwft-core/SKILL.md) for full PCO instructions and examples.

---

## ⚡ Dynamic Skill Router

The [skill_router.py](./skill_router.py) script is a standalone Python utility designed for custom agent pipelines. It implements dynamic system instruction compilation to eliminate prompt input token overhead.

### Key Capabilities
* **Option 1: Short Flags**: Extract explicit instructions from brackets (e.g., `[fwft-core]`).
* **Option 2: Skill IDs**: Use lightweight IDs (e.g., `[S01, S02]`) to compile system prompts.
* **Option 3: Dynamic Skill Loading**: Automatically load relevant instructions based on semantic keyword classification in the user prompt.
* **Option 4: Compressed Skills**: Minimize each registered skill prompt into ultra-short, dense instruction lists.
* **Option 5: Hierarchical Inheritance**: Automatically resolve dependencies (e.g., loading `fwft-core` automatically when loading `coding-standards`).

### Usage Example
```python
from skill_router import SkillRouter

router = SkillRouter()
prompt = "[fwft-core] Refactor this logic"

system_prompt, loaded_skills, raw_tokens, optimized_tokens = router.route(prompt)
cleaned_prompt = router.clean_query(prompt)

# Outputs:
# loaded_skills = ['FWFT Core']
# cleaned_prompt = "Refactor this logic"
```

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
