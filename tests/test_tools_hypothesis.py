from hypothesis import given
from hypothesis import strategies as st
from smart_file_agent.agent.tools import bulletify, summarise_text


@given(st.text())
def test_summarise_never_crashes(text):
    """
    Property test verifying summarise_text accepts any 
    string input and returns a string containing 'Summary:'.
    """

    summary = summarise_text(text)
    assert isinstance(summary, str)
    assert "Summary:" in summary

@given(st.text())
def test_bulletify_never_crashes(text):
    """
    Property test verifying bulletify accepts any string 
    input without raising exceptions and returns a string.
    """
    
    bullets = bulletify(text)
    assert isinstance(bullets, str)
