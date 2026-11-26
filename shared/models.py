
from typing import TypedDict


class Job(TypedDict):
    id: str
    title: str
    company: str
    location: str
    technologies: list[str]
    url: str


class UserPreferences(TypedDict):
    preferred_roles: list[str]
    technologies: list[str]
    preferred_location: str
    excluded_preferences: list[str]
