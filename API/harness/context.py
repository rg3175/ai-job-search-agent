
from API.harness.memory import load_memory


SYSTEM_PROMPT = """
You are a helpful job-search assistant.

Your task is to help users find suitable job opportunities.

You can:
- Search for jobs.
- Save interesting jobs.
- Remember user preferences.
- Recommend jobs based on the user's skills and preferences.

Always consider the user's saved preferences when searching for jobs.
Ask clarifying questions when important information is missing.
Do not invent job openings or company details.
"""


def build_system_prompt() -> str:
    memory = load_memory()

    memory_context = f"""
User's saved preferences:
- Preferred roles: {memory.get("preferred_roles", [])}
- Technologies: {memory.get("technologies", [])}
- Preferred location: {memory.get("preferred_location", "")}
- Excluded preferences: {memory.get("excluded_preferences", [])}
"""

    print("[context.py] System prompt and memory context prepared.")

    return SYSTEM_PROMPT + "\n" + memory_context


def build_messages(history: list[dict], user_message: str) -> list[dict]:
    messages = history.copy()

    messages.append({
        "role": "user",
        "content": user_message
    })

    print(f"[context.py] Built context with {len(messages)} messages.")

    return messages
