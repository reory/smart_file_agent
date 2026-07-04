from smart_file_agent.agent.output import format_markdown

def test_format_markdown_outputs_expected_structure():
    output = {
        "metadata": {"name": "file.txt"},
        "mode": "standard_summary",
        "steps": ["extract_text", "summarise"],
        "summary": "Summary:\n- Hello"
    }

    md = format_markdown(output)

    assert md.startswith("# Summary of file.txt")
    assert "**Mode:** standard_summary" in md
    assert "extract_text, summarise" in md
    assert "Hello" in md

