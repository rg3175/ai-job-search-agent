# AI Job Search Agent
### Comparing Custom Anthropic API Harness and Claude Agent SDK

## Overview

AI Job Search Agent is a Python-based project that demonstrates two approaches to building an AI-powered job search assistant:

- **Custom Anthropic API Harness** – An agent implemented using the Anthropic Messages API with a custom conversation loop and tool execution.
- **Claude Agent SDK** – An alternative implementation using the Claude Agent SDK and MCP tool integration.

The agent is designed to help users search for job opportunities, save interesting positions, retrieve saved jobs, and maintain personal job-search preferences.

The primary target role is Full Stack Developer, with additional interest in Backend and AI positions.

## Features

- Search for job opportunities using an external job-board API.
- Save and retrieve job opportunities.
- Update user preferences.
- Persistent JSON-based memory.
- Conversation history management.
- Custom tool integration.
- Context construction and management.
- Token usage recording for API responses.
- Offline testing support.

## Project Structure

```text
job-agent/
│
├── API/
│   ├── harness/
│   │   ├── loop.py
│   │   ├── tools.py
│   │   ├── history.py
│   │   ├── memory.py
│   │   ├── context.py
│   │   ├── compaction.py
│   │   ├── caching.py
│   │   └── tokens.py
│   ├── agent.py
│   └── main.py
│
├── SDK/
│   ├── agent.py
│   ├── tools.py
│   ├── offline_agent.py
│   ├── offline_main.py
│   └── run_scenario.py
│
├── shared/
│   ├── models.py
│   ├── storage.py
│   └── tools.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_memory.py
│   ├── test_offline_agent.py
│   └── test_shared_tools.py
│
├── data/
├── results/
├── scenario.json
├── REPORT.md
└── requirements.txt
```

## Technologies

- Python 3.12
- Anthropic Messages API
- Claude Agent SDK
- MCP (Model Context Protocol)
- JSON-based persistent storage
- Pytest
- External Job Board API

## Installation

Clone the repository:

```bash
git clone https://github.com/rg3175/ai-job-search-agent.git
cd ai-job-search-agent
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### Custom API Agent

```bash
python -m API.main
```

Live execution requires a valid Anthropic API key and an account with available API credit.

### Offline Scenario

```bash
python -m SDK.run_scenario
```

This runs the local memory persistence scenario without requiring a live model request.

## Running Tests

Execute the automated test suite:

```bash
python -m pytest -v
```

The current test suite includes 6 passing tests covering memory persistence, shared tools, saved jobs, and offline agent behavior.

## API vs SDK

| Custom API Harness | Claude Agent SDK |
|---|---|
| Custom conversation loop | SDK-based agent interaction |
| Custom tool dispatch | SDK tool integration |
| Custom context construction | SDK system prompt |
| Custom history management | Shared history storage |
| Direct control over execution | Higher-level abstractions |

## Testing and Limitations

The automated test suite currently passes all 6 tests.

Python compilation checks also complete successfully.

Live model execution and real token-cost measurements were not verified because the Anthropic API account did not have sufficient credit.

The external job search functionality also depends on network connectivity and external API availability.

The offline implementation is intended for local testing and does not replace live LLM execution.

For additional implementation details and the project comparison, see [REPORT.md](REPORT.md).

## Author

Developed as a project exploring AI agents, tool integration, persistent memory, context engineering, and the differences between API-based and SDK-based agent architectures.
