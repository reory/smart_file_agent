from hypothesis import given, strategies as st
from smart_file_agent.agent.tools import summarise_text, bulletify

@given(st.text())
def test_summarise_never_crashes(text):
    summary = summarise_text(text)
    assert isinstance(summary, str)
    assert "Summary:" in summary

@given(st.text())
def test_bulletify_never_crashes(text):
    bullets = bulletify(text)
    assert isinstance(bullets, str)
