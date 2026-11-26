
import os
import asyncio

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ResultMessage,
    AssistantMessage,
    TextBlock,
    create_sdk_mcp_server,
    query
)

from SDK.tools import (
    search_jobs,
    save_job,
    get_saved_jobs,
    update_preferences
)

from API.harness.memory import load_memory
from API.harness.history import load_history, save_history


SYSTEM_PROMPT = """
You are a helpful AI job-search assistant.

Your primary goal is to help users find suitable Full Stack Developer jobs.
Backend and AI positions are also relevant.

You can:
- Search for jobs.
- Save interesting jobs.
- Retrieve saved jobs.
- Update user preferences.

Always consider the user's saved preferences.
Never invent job openings or company details.
Ask questions when important information is missing.
"""


class JobSearchSDKAgent:

    def __init__(self, session_id="sdk_default"):
        self.session_id = session_id

        self.model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-sonnet-5-5"
        )

        self.history = load_history(session_id)

        self.tool_server = create_sdk_mcp_server(
            name="job_search",
            version="1.0.0",
            tools=[
                search_jobs,
                save_job,
                get_saved_jobs,
                update_preferences
            ]
        )

        self.options = ClaudeAgentOptions(
            model=self.model,
            system_prompt=SYSTEM_PROMPT,
            mcp_servers={"job_search": self.tool_server},
            allowed_tools=[
                "mcp__job_search__search_jobs",
                "mcp__job_search__save_job",
                "mcp__job_search__get_saved_jobs",
                "mcp__job_search__update_preferences"
            ],
            setting_sources=[]
        )

        print(f"[SDK agent] Initialized with model: {self.model}")

    async def _ask(self, prompt):
        final_answer = []

        async for message in query(
            prompt=prompt,
            options=self.options
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        final_answer.append(block.text)

            if isinstance(message, ResultMessage):
                if message.result:
                    return message.result

        return "\n".join(final_answer)

    def chat(self, user_message):
        memory = load_memory()

        context = f"""
User preferences:
- Preferred roles: {memory.get("preferred_roles", [])}
- Technologies: {memory.get("technologies", [])}
- Preferred location: {memory.get("preferred_location", "")}
- Excluded preferences: {memory.get("excluded_preferences", [])}
"""

        conversation = ""

        for message in self.history:
            role = message.get("role", "user")
            content = message.get("content", "")

            if isinstance(content, str):
                conversation += f"\n{role}: {content}"

        prompt = f"""
{context}

Previous conversation:
{conversation}

New user message:
{user_message}
"""

        answer = asyncio.run(self._ask(prompt))

        self.history.append({
            "role": "user",
            "content": user_message
        })

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        save_history(self.session_id, self.history)

        return answer
