
from claude_agent_sdk import tool
from shared import tools as shared_tools


@tool(
    "search_jobs",
    "Search for job opportunities by role, technology, or location.",
    {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "location": {"type": "string"},
            "limit": {"type": "integer"}
        },
        "required": []
    }
)
async def search_jobs(args):
    result = shared_tools.search_jobs(
        query=args.get("query", ""),
        location=args.get("location", ""),
        limit=args.get("limit", 10)
    )
    return {"content": [{"type": "text", "text": str(result)}]}


@tool(
    "save_job",
    "Save a job opportunity to the user's saved jobs.",
    {
        "type": "object",
        "properties": {
            "job": {"type": "object"}
        },
        "required": ["job"]
    }
)
async def save_job(args):
    result = shared_tools.save_job(args["job"])
    return {"content": [{"type": "text", "text": str(result)}]}


@tool(
    "get_saved_jobs",
    "Get all jobs previously saved by the user.",
    {
        "type": "object",
        "properties": {},
        "required": []
    }
)
async def get_saved_jobs(args):
    result = shared_tools.get_saved_jobs()
    return {"content": [{"type": "text", "text": str(result)}]}


@tool(
    "update_preferences",
    "Update the user's job search preferences.",
    {
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
            "preferred_location": {"type": "string"},
            "excluded_preferences": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": []
    }
)
async def update_preferences(args):
    result = shared_tools.update_preferences(
        preferred_roles=args.get("preferred_roles"),
        technologies=args.get("technologies"),
        preferred_location=args.get("preferred_location"),
        excluded_preferences=args.get("excluded_preferences")
    )
    return {"content": [{"type": "text", "text": str(result)}]}
