
import json
from pathlib import Path
from datetime import datetime, timezone

from shared import tools as shared_tools


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCENARIO_FILE = PROJECT_ROOT / "scenario.json"
RESULTS_FILE = PROJECT_ROOT / "results" / "scenario_results.json"


def main():
    with SCENARIO_FILE.open("r", encoding="utf-8") as file:
        scenario = json.load(file)

    expected = scenario["expected_memory"]

    print("=" * 45)
    print("Running Job Search Memory Scenario")
    print("=" * 45)

    # Session 1: Save preferences
    print("\nStarting session 1")

    save_result = shared_tools.update_preferences(
        preferred_roles=expected["preferred_roles"],
        technologies=expected["technologies"],
        preferred_location=expected["preferred_location"],
        excluded_preferences=expected["excluded_preferences"]
    )

    # Session 2: Load preferences again
    print("\nStarting session 2")

    load_result = shared_tools.update_preferences()
    actual = load_result.get("preferences", {})

    success = actual == expected

    result = {
        "scenario_name": scenario["scenario_name"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sessions_tested": 2,
        "expected_memory": expected,
        "actual_memory": actual,
        "save_result": save_result,
        "success": success
    }

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with RESULTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    print("\nExpected:", expected)
    print("Actual:", actual)
    print("\nSUCCESS!" if success else "\nFAILED!")
    print(f"Results saved to: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
