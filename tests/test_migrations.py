import sqlite3
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER_MIGRATION = ROOT / "migrations" / "0001_create_schema_migrations.sql"


class MigrationLedgerTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")

    def tearDown(self):
        self.connection.close()

    def test_reference_migration_applies_to_fresh_database(self):
        self.connection.executescript(LEDGER_MIGRATION.read_text(encoding="utf-8"))
        row = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type = ? AND name = ?",
            ("table", "schema_migrations"),
        ).fetchone()
        self.assertEqual(row, ("schema_migrations",))

    def test_ledger_accepts_migration_metadata(self):
        self.connection.executescript(LEDGER_MIGRATION.read_text(encoding="utf-8"))
        self.connection.execute(
            """
            INSERT INTO schema_migrations (version, name, checksum, applied_at)
            VALUES (?, ?, ?, ?)
            """,
            ("0001", "create_schema_migrations", "abc123", "2026-10-28T00:00:00Z"),
        )
        self.connection.commit()
        row = self.connection.execute(
            "SELECT version, name, checksum, applied_at FROM schema_migrations"
        ).fetchone()
        self.assertEqual(
            row,
            ("0001", "create_schema_migrations", "abc123", "2026-10-28T00:00:00Z"),
        )

    def test_ledger_requires_all_metadata_fields(self):
        self.connection.executescript(LEDGER_MIGRATION.read_text(encoding="utf-8"))
        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                "INSERT INTO schema_migrations (version, name, checksum) VALUES (?, ?, ?)",
                ("0001", "create_schema_migrations", "abc123"),
            )

    def test_ledger_rejects_duplicate_versions(self):
        self.connection.executescript(LEDGER_MIGRATION.read_text(encoding="utf-8"))
        entry = (
            "0001",
            "create_schema_migrations",
            "abc123",
            "2026-10-28T00:00:00Z",
        )
        self.connection.execute(
            """
            INSERT INTO schema_migrations (version, name, checksum, applied_at)
            VALUES (?, ?, ?, ?)
            """,
            entry,
        )
        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                """
                INSERT INTO schema_migrations (version, name, checksum, applied_at)
                VALUES (?, ?, ?, ?)
                """,
                entry,
            )


if __name__ == "__main__":
    unittest.main()
