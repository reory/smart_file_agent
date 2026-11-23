# Contributing to Smart File Agent

Thank you for your interest in contributing to Smart File Agent.

Smart File Agent is a deliberately small, educational project that demonstrates how an agentic AI pipeline works using pure Python. The goal is to show the mechanics behind ingestion, reasoning, planning, tool execution, and output generation without relying on external AI services or large frameworks.

Contributions that improve clarity, maintainability, testing, documentation, or learning value are always welcome.

---

## Project Philosophy

This project is designed to help developers understand how agent-style systems operate internally.

The pipeline consists of:

1. File Ingestion
2. Request Analysis
3. Planning
4. Tool Execution
5. Output Generation

The emphasis is on readability and education rather than complexity.

When contributing, please favor:

- Simple solutions
- Clear code
- Strong documentation
- Good test coverage
- Small, focused changes

---

## Development Setup

This project uses **uv** for dependency management.

### Clone the Repository

```bash
git clone https://github.com/reory/smart_file_agent.git
cd smart_file_agent
```

### Synchronise Dependencies

```bash
uv sync
```

---

## Running the Application

Start the Smart File Agent from the project root:

```bash
uv run python -m smart_file_agent.main
```

The application will prompt for:

- A file path
- A user request

Example requests:

```text
summarise this
```

```text
give me a summary
```

```text
bulletify
```

```text
turn this into bullet points
```

---

## Running Tests

Run the full test suite:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

The project currently uses:

- pytest
- pytest-cov
- hypothesis

All tests should pass before submitting a pull request.

---

## Code Style Guidelines

Please follow standard Python conventions:

- Follow PEP 8
- Keep functions small and focused
- Prefer readability over cleverness
- Use descriptive names
- Add tests for new functionality
- Add docstrings where appropriate

Example:

```python
def analyse_request(prompt: str) -> str:
    """Determine the processing mode from a user request."""
```

---

## Good Contributions

Examples of contributions that fit this project well:

✅ Documentation improvements

✅ Additional tests

✅ Better error handling

✅ Small self-contained tools

✅ Refactoring that improves readability

✅ Educational examples

✅ Improved logging or diagnostics

✅ Performance improvements that do not reduce readability

---

## Contributions to Avoid

This repository is intentionally lightweight and educational.

Please avoid introducing:

❌ Large frameworks

❌ Unnecessary dependencies

❌ Complex abstractions

❌ Features that obscure how the agent works

❌ AI API integrations that replace the learning experience

❌ Changes that significantly increase maintenance burden

If a feature makes the project substantially harder to understand, it is probably not a good fit.

---

## Pull Requests

Before opening a pull request:

- Ensure all tests pass
- Add tests for any new functionality
- Update documentation if necessary
- Keep changes focused on a single goal
- Remove unused code and debug statements

A good pull request should explain:

1. What changed
2. Why the change was made
3. How the change was tested

---

## Reporting Issues

If you discover a bug or have an improvement suggestion:

1. Search existing issues first
2. Create a new issue if necessary
3. Provide steps to reproduce the problem
4. Include expected and actual behaviour

Clear issue reports help maintain the project efficiently.

---

## Feature Ideas

Ideas for future improvements include:

- Memory systems
- Tool registries
- Additional text-processing tools
- FastAPI interfaces
- Extended output formats

Please open an issue before starting major feature work so the design can be discussed first.

---

## License

By contributing to this project, you agree that your contributions will be released under the project's MIT License.

---

Built by Roy Peters 😁