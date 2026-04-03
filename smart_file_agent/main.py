# Simple CLI entry point. (Command Line Interface)

from smart_file_agent.agent.agent_core import run_agent
from smart_file_agent.agent.output import format_markdown
from .agent.logging_config import setup_logging
import logging
logger = logging.getLogger(__name__)

setup_logging()


def main():
    logger.info("CLI started")
    file_path = input("Enter file path: ").strip()
    prompt = input("What would you like to do? ").strip()
    print()
    
    output = run_agent(file_path, prompt)
    md = format_markdown(output)
    
    logger.info("Agent returned output successfully")
    print("\n" + "="*60)
    print("AGENT OUTPUT")
    print("="*60 + "\n")
    print(md)
    print("\n" + "="*60 + "\n")
   


if __name__ == "__main__":
    main()