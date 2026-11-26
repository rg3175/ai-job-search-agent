
from shared.storage import load_json, save_json


def test_memory_persists_between_sessions(tmp_path, monkeypatch):
    import API.harness.memory as memory_module

    memory_file = tmp_path / "agent_memory.json"
    monkeypatch.setattr(memory_module, "MEMORY_FILE", memory_file)

    preferences = {
        "preferred_roles": ["Full Stack Developer"],
        "technologies": ["Python", "JavaScript"],
        "preferred_location": "Israel",
        "excluded_preferences": []
    }

    memory_module.save_memory(preferences)

    loaded_memory = memory_module.load_memory()

    assert loaded_memory == preferences
    assert loaded_memory["preferred_roles"] == ["Full Stack Developer"]
    assert loaded_memory["technologies"] == ["Python", "JavaScript"]
