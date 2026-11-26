
import os
from anthropic import Anthropic

from API.harness.history import load_history, save_history
from API.harness.context import build_system_prompt, build_messages
from API.harness.loop import run_conversation
from API.harness.caching import create_cache_key
from API.harness.tools import TOOLS


class JobSearchAgent:
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id
        self.model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-sonnet-5-5"
        )

        self.client = Anthropic()
        self.history = load_history(session_id)

        print(f"[agent.py] Agent initialized with model: {self.model}")

    def chat(self, user_message: str) -> str:
        system_prompt = build_system_prompt()

        cache_key = create_cache_key(
            system_prompt,
            TOOLS,
            self.model
        )
        print(f"[agent.py] Context key: {cache_key[:12]}")

        messages = build_messages(
            self.history,
            user_message
        )

        answer, updated_history = run_conversation(
            client=self.client,
            model=self.model,
            system_prompt=system_prompt,
            messages=messages,
            session_id=self.session_id
        )

        self.history = updated_history
        save_history(self.session_id, self.history)

        return answer
