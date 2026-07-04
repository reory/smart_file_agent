from smart_file_agent.agent.processing import analyse_request, plan_steps

def test_analyse_request_standard():
    assert analyse_request("summarise this") == "standard_summary"

def test_analyse_request_bullet():
    assert analyse_request("bulletify please") == "bullet_summary"

def test_plan_steps_standard():
    assert plan_steps("standard_summary") == ["extract_text", "summarise"]

def test_plan_steps_bullet():
    assert plan_steps("bullet_summary") == ["extract_text", "summarise", "bulletify"]
