import builtins
from unittest.mock import patch
from smart_file_agent.main import main

def test_main_runs_agent_and_prints_output(tmp_path):
    
    # Create a temporary file for the agent to read
    file = tmp_path / "demo.txt"
    file.write_text("Python is great.")

    # Mock user input
    inputs = [str(file), "summarise this"]

    with patch.object(builtins, "input", side_effect=inputs):
        with patch("builtins.print") as mock_print:
            main()
            # Ensure something was printed
            assert mock_print.call_count > 0
