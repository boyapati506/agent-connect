from pathlib import Path

PROMPT_DIR = Path(__file__).parent

def load_system_prompt() -> str:
    prompt_path = PROMPT_DIR / "system" / "agentconnect.md"
    return prompt_path.read_text(encoding="utf-8")

