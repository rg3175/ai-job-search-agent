
import hashlib
import json


def create_cache_key(system_prompt: str, tools: list, model: str) -> str:
    """
    Creates a stable key for identical API request context.
    """
    content = {
        "system": system_prompt,
        "tools": tools,
        "model": model
    }

    serialized = json.dumps(
        content,
        sort_keys=True,
        ensure_ascii=False
    )

    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def estimate_cacheable_tokens(system_prompt: str) -> int:
    """
    Rough estimate only: approximately 4 characters per token.
    """
    return max(1, len(system_prompt) // 4)
