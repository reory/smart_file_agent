# The “agentic brain.”

import logging
from .ingestion import load_file, extract_metadata
from .processing import analyse_request, plan_steps
from .tools import summarise_text, bulletify

logger = logging.getLogger(__name__)

def run_agent(file_path: str, user_prompt: str) -> dict:
    """
    Core agent - 
    Handles ingestion - reasoning - planning - tool execution - output.
    """

    logger.info("Starting agent pipeline")
    logger.info(f"Loading file: {file_path}")

    # Ingest
    text = load_file(file_path)
    metadata = extract_metadata(file_path)
    logger.info("File loaded successfully")
    
    # Reasoning
    mode = analyse_request(user_prompt)
    logger.info(f"Detected mode: {mode}")

    # Planning
    steps = plan_steps(mode)
    logger.info(f"Planned steps: {steps}")
    
    # Action layer (tool execution)
    output = text
    for step in steps:
        logger.info(f"Executing step: {step}")

        if step == "summarise":
            output = summarise_text(output)
        elif step == "bulletify":
            output = bulletify(output)
    
    logger.info("Pipeline complete")
    
    # Output
    return {
        "metadata": metadata,
        "summary": output,
        "mode": mode,
        "steps": steps
    }