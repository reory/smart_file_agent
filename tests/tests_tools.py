from smart_file_agent.agent.tools import summarise_text, bulletify

def test_summarise_text_basic():
    text = "Python is great. It is used everywhere."
    summary = summarise_text(text)
    assert "Summary:" in summary
    assert "Keywords:" in summary

def test_summarise_empty():
    assert "empty" in summarise_text("")

def test_bulletify():
    text = "Summary:\n- Opening idea: Python is great.\n- Key detail: It is used everywhere."
    bullets = bulletify(text)
    assert "- Python is great" in bullets
    assert "- It is used everywhere" in bullets
