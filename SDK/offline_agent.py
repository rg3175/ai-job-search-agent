
from shared import tools as shared_tools


class OfflineJobSearchAgent:
    """A local agent for testing job-search tools without an API call."""

    def chat(self, user_message: str) -> str:
        message = user_message.strip().lower()

        # Check saved jobs before general job search
        if "שמורות" in message or "saved" in message:
            result = shared_tools.get_saved_jobs()
            return f"המשרות השמורות שלך:\n{result}"

        if "העדפות" in message or "preferences" in message:
            result = shared_tools.update_preferences(
                preferred_roles=["Full Stack Developer"],
                technologies=["Python", "JavaScript"],
                preferred_location="Israel"
            )
            return f"ההעדפות עודכנו:\n{result}"

        if "משרות" in message or "חפש" in message or "job" in message:
            result = shared_tools.search_jobs(limit=5)
            return f"תוצאות חיפוש מקומיות:\n{result}"

        return (
            "אני פועל כרגע במצב Offline.\n"
            "אפשר לכתוב: חפש משרות, הצג משרות שמורות או עדכן העדפות."
        )
