import tempfile
from pathlib import Path
from smart_file_agent.agent.ingestion import load_file, extract_metadata

def test_load_file_reads_contents():
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "hello.txt"
        file.write_text("hello world")
        assert load_file(str(file)) == "hello world"

def test_extract_metadata():
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "data.txt"
        file.write_text("content")
        meta = extract_metadata(str(file))
        assert meta["name"] == "data.txt"
        assert meta["extension"] == ".txt"
        assert meta["size_kb"] > 0

