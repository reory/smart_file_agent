# Handles query analysis, planning, and LLM reasoning.
import logging
logger = logging.getLogger(__name__)

def analyse_request(user_prompt: str) -> str:

    logger.info(f"Analysing user request: {user_prompt}")

    if "bullet" in user_prompt.lower():
        return "bullet_summary"
    return "standard_summary"

def plan_steps(mode: str) -> list:

    if mode == "bullet_summary":
        return ["extract_text", "summarise", "bulletify"]
    return ["extract_text", "summarise"]