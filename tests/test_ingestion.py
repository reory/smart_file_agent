import tempfile
from pathlib import Path

from smart_file_agent.agent.ingestion import extract_metadata, load_file


def test_load_file_reads_contents():
    """
    Test that load_file correctly reads and 
    returns text content from a target file.
    """

    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "hello.txt"
        file.write_text("hello world")

        content, resolved_path = load_file(str(file))
        assert content == "hello world"
        assert resolved_path == file


def test_extract_metadata():
    """
    Test that extract_metadata retrieves filename, 
    file extension, and non-zero size.
    """
    
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "data.txt"
        file.write_text("content")
        meta = extract_metadata(str(file))
        assert meta["name"] == "data.txt"
        assert meta["extension"] == ".txt"
        assert meta["size_kb"] > 0

