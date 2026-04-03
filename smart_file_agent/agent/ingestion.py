from pathlib import Path
import logging
logger = logging.getLogger(__name__)

# Handles file loading, metadata, logs.

def load_file(path: str) -> str:

    logger.info(f"Reading file {path}")

    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    return text

def extract_metadata(path: str) -> dict:

    file_path = Path(path)
    return {
        "name": file_path.name,
        "size_kb": round(file_path.stat().st_size / 1024, 2),
        "extension": file_path.suffix,
    }
