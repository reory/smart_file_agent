from smart_file_agent.agent.memory import MemoryState


def test_memory_can_store_and_search(tmp_path):

    db_path = tmp_path / "test_memory.db"

    memory = MemoryState(db_path)

    memory.remember(
        file_path="notes.txt",
        summary="Pytest fixtures improve testing",
        keywords="pytest testing",
        processed_at="2026-11-10",
    )

    results = memory.search("pytest")

    assert len(results) == 1
    assert results[0][0] == "notes.txt"