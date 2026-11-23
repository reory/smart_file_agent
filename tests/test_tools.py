from smart_file_agent.agent.tools import bulletify, summarise_text


def test_summarise_text_basic():
    """
    Test that summarise_text formats non-empty 
    text with summary and keyword sections.
    """

    text = "Python is great. It is used everywhere."
    summary = summarise_text(text)
    assert "Summary:" in summary
    assert "Keywords:" in summary

def test_summarise_empty():
    """Test that summarise_text handles empty input string gracefully."""

    assert "empty" in summarise_text("")

def test_bulletify():
    """Test that bulletify extracts key points into bulleted output format."""
    
    text = "Summary:\n- Opening idea: Python is great.\n- Key detail: It is used everywhere."
    bullets = bulletify(text)
    assert "- Python is great" in bullets
    assert "- It is used everywhere" in bullets
