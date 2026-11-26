
def compact_messages(messages: list[dict], keep_last: int = 12) -> list[dict]:
    """
    Keeps the latest conversation messages when history becomes too long.
    """
    if len(messages) <= keep_last:
        return messages

    recent_messages = messages[-keep_last:]

    # Start from a regular user message to avoid a partial tool exchange.
    for index, message in enumerate(recent_messages):
        content = message.get("content", "")

        if message.get("role") == "user" and isinstance(content, str):
            return recent_messages[index:]

    return recent_messages
