# AI Job Search Agent – API vs SDK

## 1. Project Overview

This project implements an AI-powered Job Search Agent using two different approaches:

1. **Custom Anthropic API Harness** – A custom agent architecture built on top of the Anthropic Messages API.
2. **Claude Agent SDK** – An alternative implementation using the Claude Agent SDK and its tool integration capabilities.

The agent is designed to help users discover relevant job opportunities, save interesting positions, retrieve saved jobs, and maintain job-search preferences across sessions.

The primary target role is **Full Stack Developer**, with additional interest in Backend and AI positions.

## 2. System Architecture

The project is organized into three main parts:

- `API/` – Custom API-based agent implementation.
- `SDK/` – Claude Agent SDK implementation.
- `shared/` – Shared business logic, data models, and storage functionality.

### Shared Components

Both implementations use shared functionality to reduce code duplication:

- Job search using an external job-board API.
- Saving job opportunities.
- Retrieving saved jobs.
- Updating user preferences.
- Persistent JSON-based storage.
- Reusable job and preference data models.

## 3. Custom API Harness

The API implementation provides direct control over the agent execution process.

Its components include:

- **loop.py** – Manages the conversation loop and tool execution.
- **tools.py** – Defines tool schemas and dispatches tool calls.
- **history.py** – Loads and saves conversation history.
- **memory.py** – Manages persistent user preferences.
- **context.py** – Builds the system prompt and conversation context.
- **compaction.py** – Limits conversation history to control context size.
- **caching.py** – Generates a context cache key and estimates cacheable tokens.
- **tokens.py** – Records input and output token usage when an API response is received.

This approach provides flexibility and control over the agent's internal behavior.

## 4. Claude Agent SDK

The SDK implementation uses the Claude Agent SDK to simplify agent development.

It includes:

- Custom tools defined with the SDK tool decorator.
- MCP server integration.
- Tool access configuration.
- Conversation history management.
- Loading saved user preferences.
- Persistent JSON storage through shared components.

The SDK reduces the amount of custom infrastructure required for tool integration and agent interactions.

## 5. Memory and Context Engineering

The project uses persistent JSON files to store user preferences and saved job opportunities.

Preferences include:

- Preferred job roles.
- Preferred technologies.
- Preferred location.
- Excluded job preferences.

The stored information can be loaded in a new session, allowing the agent to reuse previously saved preferences.

The API implementation also separates context construction from conversation execution.

## 6. Testing and Validation

The project includes automated tests covering:

- Memory persistence between sessions.
- Retrieving saved jobs.
- Updating user preferences.
- Offline agent behavior.
- Shared business logic.

**Test results:**
- 6 automated tests passed.
- 0 test failures.
- Python compilation checks completed successfully for API, SDK, shared, and tests directories.

A separate memory scenario was also executed to verify that preferences could be saved and loaded again.

## 7. Limitations

Some functionality could not be fully validated in a live environment:

- Live Anthropic model execution was not completed because the API account had insufficient credit.
- External job search depends on network connectivity and the availability of the external job-board API.
- Token usage recording is implemented for successful API responses, but actual live token measurements were not collected.
- The caching component generates a cache key and estimates cacheable tokens; actual provider-side prompt caching was not verified.
- The offline agent supports local testing but does not replace a live LLM-powered agent.

Therefore, live model performance and actual API costs are not reported.

## 8. API vs SDK Comparison

| Aspect | Custom API Harness | Claude Agent SDK |
|---|---|---|
| Conversation management | Custom implementation | SDK-managed interaction |
| Tool integration | Custom schemas and dispatch | SDK tools and MCP server |
| Memory | Custom persistent storage | Shared persistent storage |
| Context management | Custom context construction | Context supplied to SDK |
| Token tracking | Custom usage recording | Not independently measured |
| Development complexity | Higher | Lower |
| Flexibility | Greater control | Higher-level abstraction |

## 9. Conclusion

This project demonstrates two architectural approaches to building an AI-powered job search agent.

The Custom API Harness provides greater control over conversation flow, context construction, tool execution, and token tracking.

The Claude Agent SDK simplifies agent development by providing built-in abstractions for tool integration and agent interactions.

Using shared business logic ensures that both implementations rely on the same core job-search functionality and persistent data structures.

The project also demonstrates practical concepts in agent development, including tool calling, persistent memory, context engineering, modular architecture, automated testing, and API/SDK comparison.