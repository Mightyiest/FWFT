import re
from typing import Dict, List, Set, Tuple

# Skill Database representing local storage of full instructions
SKILL_DATABASE: Dict[str, Dict[str, str]] = {
    "S01": {
        "tag": "fwft-core",
        "name": "FWFT Core",
        "prompt": "FWFT_CORE:\n- Minimal tokens\n- No fluff\n- Direct answers\n- Markdown only if useful"
    },
    "S02": {
        "tag": "coding-standards",
        "name": "Coding Standards",
        "prompt": "CODING_STANDARDS:\n- PEP8 compliance\n- Strict typing\n- Docstrings for public APIs\n- Clean error handling"
    },
    "S03": {
        "tag": "report-writer",
        "name": "Report Writer",
        "prompt": "REPORT_WRITER:\n- Clear executive summary\n- Structured markdown tables\n- Actionable recommendations\n- Bulleted key findings"
    },
    "S04": {
        "tag": "ui-designer",
        "name": "UI Designer",
        "prompt": "UI_DESIGNER:\n- Mobile-first responsive layouts\n- Clean CSS custom properties\n- Semantic HTML5 structural elements\n- Accessible contrast ratios"
    },
    "S05": {
        "tag": "database-expert",
        "name": "Database Expert",
        "prompt": "DATABASE_EXPERT:\n- Optimized indexes\n- Normalization up to 3NF\n- Prevent SQL injection\n- Explicit transaction control"
    }
}

# Hierarchical skill inheritance mapping
HIERARCHICAL_INHERITANCE: Dict[str, List[str]] = {
    "coding-standards": ["fwft-core"],
    "report-writer": ["fwft-core"],
    "ui-designer": ["fwft-core"],
    "database-expert": ["fwft-core"]
}

# Keywords to support Option 3: Dynamic Skill Loading
DYNAMIC_KEYWORDS: Dict[str, List[str]] = {
    "coding-standards": ["def ", "class ", "function", "import ", "code", "refactor"],
    "report-writer": ["report", "summary", "csv", "data analysis", "findings"],
    "ui-designer": ["css", "html", "flexbox", "grid", "component", "button", "frontend"],
    "database-expert": ["sql", "query", "database", "table", "index", "postgresql", "mysql"]
}

class SkillRouter:
    """
    Implements a token-optimized Skill Router for Agent Systems.
    Reduces prompt overhead by dynamically matching and injecting only required skills.
    """

    def __init__(self, skill_db: Dict[str, Dict[str, str]] = SKILL_DATABASE):
        self.db = skill_db
        # Reverse lookups
        self.tag_to_id = {v["tag"]: k for k, v in self.db.items()}
        self.id_to_tag = {k: v["tag"] for k, v in self.db.items()}

    def parse_explicit_ids(self, query: str) -> Set[str]:
        """Option 2: Extract explicit skill IDs from brackets, e.g., [S01, S02]"""
        matches = re.findall(r"\[([A-Z0-9,\s]+)\]", query)
        found_ids = set()
        for match in matches:
            for part in match.split(","):
                part = part.strip()
                if part in self.db:
                    found_ids.add(part)
        return found_ids

    def parse_explicit_flags(self, query: str) -> Set[str]:
        """Option 1: Extract explicit skill tags from brackets, e.g., [lightweight-core]"""
        matches = re.findall(r"\[([a-z0-9-,\s]+)\]", query)
        found_ids = set()
        for match in matches:
            for part in match.split(","):
                part = part.strip()
                if part in self.tag_to_id:
                    found_ids.add(self.tag_to_id[part])
        return found_ids

    def detect_dynamic_skills(self, query: str) -> Set[str]:
        """Option 3: Automatically detect relevant skills based on query keywords"""
        detected_ids = set()
        query_lower = query.lower()
        for tag, keywords in DYNAMIC_KEYWORDS.items():
            if any(keyword in query_lower for keyword in keywords):
                if tag in self.tag_to_id:
                    detected_ids.add(self.tag_to_id[tag])
        return detected_ids

    def resolve_hierarchy(self, skill_ids: Set[str]) -> Set[str]:
        """Option 5: Resolve hierarchical dependencies (e.g., UI Designer implies Core)"""
        resolved = set(skill_ids)
        to_check = list(skill_ids)
        while to_check:
            current_id = to_check.pop(0)
            tag = self.id_to_tag.get(current_id)
            if tag in HIERARCHICAL_INHERITANCE:
                for parent_tag in HIERARCHICAL_INHERITANCE[tag]:
                    parent_id = self.tag_to_id.get(parent_tag)
                    if parent_id and parent_id not in resolved:
                        resolved.add(parent_id)
                        to_check.append(parent_id)
        return resolved

    def clean_query(self, query: str) -> str:
        """Removes skill metadata brackets from the user query before sending to LLM"""
        return re.sub(r"\[[a-zA-Z0-9-,\s]+\]\s*", "", query).strip()

    def route(self, user_query: str) -> Tuple[str, List[str], int, int]:
        """
        Routes and compiles the prompt.
        Returns:
            Compiled system prompt, list of loaded skills, raw prompt token estimate, optimized prompt token estimate
        """
        # Step 1: Detect explicit skills by ID or Tag
        selected_ids = self.parse_explicit_ids(user_query)
        if not selected_ids:
            selected_ids = self.parse_explicit_flags(user_query)

        # Step 2: Fallback to dynamic loading if none explicitly defined
        if not selected_ids:
            selected_ids = self.detect_dynamic_skills(user_query)

        # Default to S01 (Core) if absolutely nothing matched
        if not selected_ids:
            selected_ids = {"S01"}

        # Step 3: Resolve hierarchy (inject parent skills)
        fully_resolved_ids = self.resolve_hierarchy(selected_ids)

        # Step 4: Compile prompts
        compiled_prompts = [self.db[sid]["prompt"] for sid in sorted(fully_resolved_ids)]
        system_instruction = "\n\n".join(compiled_prompts)

        # Calculate token metrics (approximation: 1 token = 4 characters)
        all_skills_len = sum(len(v["prompt"]) for v in self.db.values())
        optimized_len = len(system_instruction)

        raw_tokens = int(all_skills_len / 4)
        optimized_tokens = int(optimized_len / 4)

        return system_instruction, [self.db[sid]["name"] for sid in sorted(fully_resolved_ids)], raw_tokens, optimized_tokens


# Example Usage Demonstration
if __name__ == "__main__":
    router = SkillRouter()
    
    test_queries = [
        "[S02] Fix the logic error in this binary search.",
        "[coding-standards] Write a script to clean up CSV data.",
        "Create a responsive flexbox navigation bar.",
        "Query the user_profiles table for active subscriptions."
    ]

    print("=== SKILL ROUTER SIMULATION ===")
    for q in test_queries:
        system_prompt, loaded_skills, raw_tok, opt_tok = router.route(q)
        clean = router.clean_query(q)
        reduction = ((raw_tok - opt_tok) / raw_tok) * 100 if raw_tok > 0 else 0
        
        print(f"\nUser Request:   '{q}'")
        print(f"Cleaned Query:  '{clean}'")
        print(f"Loaded Skills:  {', '.join(loaded_skills)}")
        print(f"Token Analysis: Raw: {raw_tok} | Optimized: {opt_tok} | Reduction: {reduction:.1f}%")
        print("-" * 50)
