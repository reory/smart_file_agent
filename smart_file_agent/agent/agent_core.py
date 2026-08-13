# The “agentic brain.”

import logging
import time

from .ingestion import extract_metadata, load_file
from .processing import analyse_request, plan_steps
from .tools import bulletify, summarise_text

logger = logging.getLogger(__name__)

def run_agent(file_path: str, user_prompt: str) -> dict:
    """
    Core agent - 
    Handles ingestion - reasoning - planning - tool execution - output.
    """

    logger.info("Starting agent pipeline")
    logger.info(f"Loading file: {file_path}")

    # Ingest
    text, actual_path = load_file(file_path)
    metadata = extract_metadata(actual_path)
    logger.info("File loaded successfully")
    
    # Reasoning
    mode = analyse_request(user_prompt)
    logger.info(f"Detected mode: {mode}")

    # Planning
    steps = plan_steps(mode)
    logger.info(f"Planned steps: {steps}")
    
    # Action layer (tool execution)
    output = text
    trace = []

    for step in steps:
        logger.info(f"Executing step: {step}")

        start_time = time.perf_counter()

        if step == "extract_text":
            result = output
            thought = "extract_text is a planning step; ingestion already provided the text"

        elif step == "summarise":
            result = summarise_text(output)
            thought = f"Mode '{mode}' requires summarising the text"
        
        elif step == "bulletify":
            result = bulletify(output)
            thought = f"Mode '{mode}' requires bulletifying the summary"

        end_time = time.perf_counter()
        duration_ms = round((end_time - start_time) * 1000, 3)

        trace.append({
            "thought": thought,
            "action": step,
            "result": result,
            "duration_ms": duration_ms
        })

        output = result

    logger.info("Pipeline complete")
    
    # Output
    return {
        "metadata": metadata,
        "summary": output,
        "mode": mode,
        "steps": steps,
        "trace": trace
    }