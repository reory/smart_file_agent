from smart_file_agent.agent.processing import analyse_request, plan_steps


def test_analyse_request_standard():
    """Test that standard summary prompt maps to 'standard_summary' mode."""

    assert analyse_request("summarise this") == "standard_summary"


def test_analyse_request_bullet():
    """Test that bullet points prompt maps to 'bullet_summary' mode."""

    assert analyse_request("bulletify please") == "bullet_summary"


def test_plan_steps_standard():
    """Test step sequence generated for 'standard_summary' mode."""

    assert plan_steps("standard_summary") == ["extract_text", "summarise"]


def test_plan_steps_bullet():
    """Test step sequence generated for 'bullet_summary' mode."""
    
    assert plan_steps("bullet_summary") == ["extract_text", "summarise", "bulletify"]
