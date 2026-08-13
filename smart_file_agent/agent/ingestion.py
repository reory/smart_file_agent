# Handles file loading, metadata, logs.
import logging
from difflib import get_close_matches
from pathlib import Path

logger = logging.getLogger(__name__)

def load_file(path: str) -> str:
    """Read file content with interactive fuzzy matching fallback for missing files."""

    logger.info(f"Reading file {path}")

    file_path = Path(path)

    if file_path.exists():
        return file_path.read_text(encoding="utf-8"), file_path
    
    # File does not exist -> fuzzy match filename
    directory = file_path.parent
    filename = file_path.name
    
    if not directory.exists():
        raise FileNotFoundError(
            f"❗Directory not found: {directory}"
        )

    files =[f.name for f in directory.iterdir() if f.is_file()]

    matches = get_close_matches(filename, files, n=1, cutoff=0.6)

    if not matches:
        raise FileNotFoundError(
            f"❗File not found: {filename}\n"
            f"No similar filenames found in: {directory}"
        )

    closest = matches[0]

    # Ask user to confirm
    print(f"❗File not found: ~{filename}")
    print(f"Closest match: {closest}")
    choice = input("Use this file instead? (y/n): ").strip().lower()

    if choice != "y":
        raise FileNotFoundError(
            "❗File not found and user declined suggested match."
        )

    correct_path = directory / closest
    logger.info(f"Using correct file: {correct_path}")

    return correct_path.read_text(encoding="utf-8"), correct_path


def extract_metadata(path: str) -> dict:
    """Extract and return metadata from the file at the given path."""

    file_path = Path(path)
    return {
        "name": file_path.name,
        "size_kb": round(file_path.stat().st_size / 1024, 2),
        "extension": file_path.suffix,
    }
