
from SDK.offline_agent import OfflineJobSearchAgent


def test_offline_agent_get_saved_jobs(monkeypatch):
    agent = OfflineJobSearchAgent()

    expected = {"success": True, "count": 0, "jobs": []}

    monkeypatch.setattr(
        "SDK.offline_agent.shared_tools.get_saved_jobs",
        lambda: expected
    )

    result = agent.chat("הצג משרות שמורות")

    assert "המשרות השמורות שלך" in result
    assert str(expected) in result


def test_offline_agent_update_preferences(monkeypatch):
    agent = OfflineJobSearchAgent()

    expected = {"success": True, "preferences": {"preferred_roles": ["Full Stack Developer"]}}

    monkeypatch.setattr(
        "SDK.offline_agent.shared_tools.update_preferences",
        lambda **kwargs: expected
    )

    result = agent.chat("עדכן העדפות")

    assert "ההעדפות עודכנו" in result
    assert str(expected) in result


def test_offline_agent_unknown_message():
    agent = OfflineJobSearchAgent()

    result = agent.chat("שלום")

    assert "מצב Offline" in result
