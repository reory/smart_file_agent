import sqlite3


class MemoryState:
    """Persist and search agent memories."""

    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()


    def create_tables(self):
        self.conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS memory
            USING fts5(
                file_path,
                summary,
                keywords,
                processed_at
            )
        """)
        self.conn.commit()


    def remember(
        self, file_path: str, 
        summary: str, keywords: str, 
        processed_at: str
    ) -> None:

        self.conn.execute(
            """
            INSERT INTO memory
            (
                file_path,
                summary,
                keywords,
                processed_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                file_path,
                summary,
                keywords,
                processed_at,
            ),
        )

        self.conn.commit()


    def search(self, query: str):

        return self.conn.execute(
            """
            SELECT
                file_path,
                summary,
                keywords
            FROM memory
            WHERE memory MATCH ?
            """,
            (query,),
        ).fetchall()