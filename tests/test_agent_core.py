import tempfile
from pathlib import Path

from smart_file_agent.agent.agent_core import run_agent


def test_run_agent_standard():
    """Test run_agent output and mode for a standard summary request."""

    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "test.txt"
        file.write_text("Python is great.")
        result = run_agent(str(file), "summarise this")
        assert result["mode"] == "standard_summary"
        assert "Summary:" in result["summary"]

def test_run_agent_bullet():
    """Test run_agent output mode and final step for a bulletify request."""
    
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "test.txt"
        file.write_text("Python is great.")
        result = run_agent(str(file), "bulletify")
        assert result["mode"] == "bullet_summary"
        assert result["steps"][-1] == "bulletify"

