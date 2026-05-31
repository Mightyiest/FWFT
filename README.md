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
│       └── SKILL.md      # Core guidelines and configuration for the FWFT skill
├── README.md             # Repository overview and documentation
└── LICENSE               # MIT License
```

---

## ⚡ Core Rules & Behavioral Matrix

| Category | Verbose / Default AI Behavior (⚠️ Avoid) | FWFT Behavior (✅ Standard) |
| :--- | :--- | :--- |
| **Response Format** | Preamble, greetings, conversational sign-offs, and summaries of what was done. | Direct output. No introductions, no conclusions, no greetings. |
| **Execution** | Explanation of plans or code before running it. | Immediate execution. |
| **Code Generation** | Step-by-step tutorial-style walkthroughs. | Raw code blocks with only essential, functional comments. |
| **File Generation** | Status messages, wrapper text, and general notes surrounding the file. | The raw file content only. |
| **Clarification** | Long, polite queries checking in on different alternatives. | Maximum 3 concise, single-sentence questions with no preamble. |

---

## 🚫 Forbidden Phrases

AI models under the **FWFT** directive must strictly avoid conversational filler and self-referential narration:

> [!WARNING]
> ### Strictly Prohibited
> * *"Thinking...", "I am thinking...", "Let me think..."*
> * *"I will...", "I'll...", "I am going to...", "Let's..."*
> * *"Here's what I'll do...", "I'll help you with..."*
> * *"Hope this helps.", "Let me know if you need anything else..."*
> * *Any conversational preamble or self-reflection.*

---

## 🛠️ Usage & Integration

### Loading as an Antigravity/Gemini Developer Skill
To use this directive as a project skill in your environment, place the `skill/fwft-core` directory inside your project's active workspace or skills path. 

```json
{
  "skills": [
    "fwft-core"
  ]
}
```

Once active, the model will prioritize token efficiency and concise responses across all automated agent workflows and developer interactions.

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
