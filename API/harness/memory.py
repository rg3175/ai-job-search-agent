
import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MEMORY_FILE = PROJECT_ROOT / "data" / "agent_memory.json"


def load_memory() -> dict:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not MEMORY_FILE.exists():
        print("[memory.py] No saved memory found.")
        return {
            "preferred_roles": [],
            "technologies": [],
            "preferred_location": "",
            "excluded_preferences": []
        }

    with MEMORY_FILE.open("r", encoding="utf-8") as file:
        memory = json.load(file)

    print("[memory.py] Memory loaded.")
    return memory


def save_memory(memory: dict[str, Any]) -> None:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with MEMORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=4)

    print("[memory.py] Memory saved.")


def update_memory(updates: dict[str, Any]) -> dict:
    memory = load_memory()

    for key, value in updates.items():
        if key in memory:
            memory[key] = value

    save_memory(memory)

    print("[memory.py] Memory updated.")
    return memory
