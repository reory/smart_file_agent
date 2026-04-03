#  Implements the actual actions the agent can perform.
import logging
logger = logging.getLogger(__name__)

def summarise_text(text: str) -> str:
    """Rule based LLM that mimics an agent."""
    logger.info("Running summarise_text tool")

    sentences = text.split(". ")
    first = sentences[0] if sentences else ""
    longest = max(sentences, key=len) if sentences else ""

    # Extract simple keywords
    words = [w.strip(".,!?").lower() for w in text.split()]
    keywords = [w for w in words if len(w) > 6][:5]

    summary = (
    "Summary:\n"
    f"- Opening idea: {first.strip()}\n"
    f"- Key detail: {longest.strip()}\n"
    f"- Keywords: {', '.join(keywords)}\n"
    )
    return summary.strip()

def bulletify(text: str) -> str:
    """Converts sentences into bullet points."""
    
    lines = text.split(". ")
    bullets = "\n".join(f"- {line.strip()}" for line in lines if line.strip())
    return bullets