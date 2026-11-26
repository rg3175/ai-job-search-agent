
import requests

from shared.storage import load_json, save_json


API_URL = "https://www.arbeitnow.com/api/job-board-api"


def search_jobs(
    query: str = "",
    location: str = "",
    limit: int = 10
) -> dict:

    try:
        response = requests.get(API_URL, timeout=20)
        response.raise_for_status()
        data = response.json().get("data", [])

    except requests.RequestException:
        return {
            "success": False,
            "error": "Could not connect to jobs API",
            "jobs": []
        }

    query_words = query.lower().split()
    results = []

    for job in data:
        title = job.get("title", "")
        company = job.get("company_name", "")
        job_location = job.get("location", "")
        tags = job.get("tags", [])

        searchable = " ".join([
            title,
            company,
            job_location,
            " ".join(tags)
        ]).lower()

        if query_words and not all(
            word in searchable for word in query_words
        ):
            continue

        if location and location.lower() not in job_location.lower():
            continue

        results.append({
            "id": job.get("slug", job.get("url", "")),
            "title": title,
            "company": company,
            "location": job_location,
            "technologies": tags,
            "url": job.get("url", "")
        })

        if len(results) >= limit:
            break

    return {
        "success": True,
        "count": len(results),
        "jobs": results
    }


def save_job(job: dict) -> dict:

    saved_jobs = load_json("saved_jobs.json", [])

    job_id = job.get("id")

    if not job_id:
        return {"success": False, "error": "Job ID is required"}

    if any(item["id"] == job_id for item in saved_jobs):
        return {"success": False, "error": "Job already saved"}

    saved_jobs.append(job)
    save_json("saved_jobs.json", saved_jobs)

    return {"success": True, "job_id": job_id}


def get_saved_jobs() -> dict:

    saved_jobs = load_json("saved_jobs.json", [])

    return {
        "count": len(saved_jobs),
        "jobs": saved_jobs
    }


def update_preferences(
    preferred_roles: list[str] | None = None,
    technologies: list[str] | None = None,
    preferred_location: str | None = None,
    excluded_preferences: list[str] | None = None
) -> dict:

    preferences = load_json(
        "memory.json",
        {
            "preferred_roles": [],
            "technologies": [],
            "preferred_location": "",
            "excluded_preferences": []
        }
    )

    updates = {
        "preferred_roles": preferred_roles,
        "technologies": technologies,
        "preferred_location": preferred_location,
        "excluded_preferences": excluded_preferences
    }

    updated_fields = []

    for key, value in updates.items():
        if value is not None:
            preferences[key] = value
            updated_fields.append(key)

    save_json("memory.json", preferences)

    return {
        "success": True,
        "updated_fields": updated_fields,
        "preferences": preferences
    }
