import logging
from smart_file_agent.agent.logging_config import setup_logging

def test_setup_logging_configures_root_logger():
    
    # Reset logging so basicConfig can apply
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.root.setLevel(logging.WARNING)

    setup_logging()

    # Root logger should now be INFO
    assert logging.root.level == logging.INFO

    # A handler should exist
    assert logging.root.handlers, "Expected at least one handler"

    handler = logging.root.handlers[0]

    # Handler level should remain NOTSET (correct behaviour)
    assert handler.level == logging.NOTSET

    # Formatter should match code format
    fmt = handler.formatter._fmt
    assert fmt == "%(asctime)s [%(levelname)s] %(message)s"

    # Date format should match
    assert handler.formatter.datefmt == "%H:%M:%S"



