
import json
from shared import tools as shared_tools


# Tools exposed to the Anthropic model
TOOLS = [
    {
        "name": "search_jobs",
        "description": "Search for job opportunities by role, technology, or location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Job title or technology to search for."
                },
                "location": {
                    "type": "string",
                    "description": "Preferred job location."
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of jobs to return."
                }
            },
            "required": []
        }
    },
    {
        "name": "save_job",
        "description": "Save a job opportunity to the user's saved jobs.",
        "input_schema": {
            "type": "object",
            "properties": {
                "job": {
                    "type": "object",
                    "description": "The job object to save."
                }
            },
            "required": ["job"]
        }
    },
    {
        "name": "get_saved_jobs",
        "description": "Get all jobs previously saved by the user.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "update_preferences",
        "description": "Update the user's job search preferences.",
        "input_schema": {
            "type": "object",
            "properties": {
                "preferred_roles": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "technologies": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "preferred_location": {
                    "type": "string"
                },
                "excluded_preferences": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": []
        }
    }
]


def execute_tool(tool_name: str, tool_input: dict) -> dict:
    """Execute a tool requested by the Anthropic model."""

    print(f"[tools.py] Executing tool: {tool_name}")

    if tool_name == "search_jobs":
        return shared_tools.search_jobs(
            query=tool_input.get("query", ""),
            location=tool_input.get("location", ""),
            limit=tool_input.get("limit", 10)
        )

    if tool_name == "save_job":
        return shared_tools.save_job(tool_input["job"])

    if tool_name == "get_saved_jobs":
        return shared_tools.get_saved_jobs()

    if tool_name == "update_preferences":
        return shared_tools.update_preferences(
            preferred_roles=tool_input.get("preferred_roles"),
            technologies=tool_input.get("technologies"),
            preferred_location=tool_input.get("preferred_location"),
            excluded_preferences=tool_input.get("excluded_preferences")
        )

    return {
        "success": False,
        "error": f"Unknown tool: {tool_name}"
    }


def serialize_tool_result(result: dict) -> str:
    """Convert a tool result into JSON text for the model."""
    return json.dumps(result, ensure_ascii=False, default=str)
