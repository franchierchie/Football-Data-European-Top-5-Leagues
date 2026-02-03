import sys
from pathlib import Path
import unittest
import sqlite3

from src.config.settings import SOURCE_DB_PATH
from src.models.raw.raw_tables import EXPECTED_SCHEMAS



class TestSourceSchema(unittest.TestCase):
  def test_source_schema_matches_expected(self) -> None:
    con = sqlite3.connect(SOURCE_DB_PATH)
    try:
      for table, expected_columns in EXPECTED_SCHEMAS.items():
        with self.subTest(table=table):
          cursor = con.execute(f"PRAGMA table_info({table});")
          actual_columns = [row[1] for row in cursor.fetchall()]
          self.assertEqual(actual_columns, expected_columns)

    finally:
      con.close()

if __name__ == "__main__":
  unittest.main()