
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
HISTORY_DIR = PROJECT_ROOT / "data" / "history"


def _get_history_path(session_id: str) -> Path:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    return HISTORY_DIR / f"{session_id}.json"


def load_history(session_id: str) -> list[dict]:
    path = _get_history_path(session_id)

    if not path.exists():
        print("[history.py] No previous history found.")
        return []

    with path.open("r", encoding="utf-8") as file:
        history = json.load(file)

    print(f"[history.py] Loaded {len(history)} messages.")
    return history


def save_history(session_id: str, messages: list[dict]) -> None:
    path = _get_history_path(session_id)

    with path.open("w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)

    print(f"[history.py] Saved {len(messages)} messages.")
