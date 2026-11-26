
from API.harness.tools import TOOLS, execute_tool, serialize_tool_result
from API.harness.tokens import record_usage
from API.harness.compaction import compact_messages


def run_conversation(
    client,
    model: str,
    system_prompt: str,
    messages: list[dict],
    session_id: str = "default"
) -> tuple[str, list[dict]]:

    messages = compact_messages(messages)

    for _ in range(8):
        response = client.messages.create(
            model=model,
            max_tokens=1500,
            system=system_prompt,
            messages=messages,
            tools=TOOLS
        )

        record_usage(response, session_id)

        assistant_content = [
            block.model_dump(exclude_none=True)
            for block in response.content
        ]

        messages.append({
            "role": "assistant",
            "content": assistant_content
        })

        tool_results = []

        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": serialize_tool_result(result)
                })

        if not tool_results:
            answer = "\n".join(
                block.text
                for block in response.content
                if block.type == "text"
            )
            return answer, messages

        messages.append({
            "role": "user",
            "content": tool_results
        })

    return "הגענו למספר הפעולות המרבי בשיחה. אפשר לנסות שוב.", messages
