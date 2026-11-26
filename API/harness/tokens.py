
import json
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parents[2]
USAGE_FILE = PROJECT_ROOT / "results" / "token_usage.json"


def record_usage(response, session_id: str = "default") -> dict:
    USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

    usage = response.usage

    record = {
        "session_id": session_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens
    }

    records = []

    if USAGE_FILE.exists():
        with USAGE_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

    records.append(record)

    with USAGE_FILE.open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

    print(
        f"[tokens.py] Input: {record['input_tokens']} | "
        f"Output: {record['output_tokens']}"
    )

    return record
