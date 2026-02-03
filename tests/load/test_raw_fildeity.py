import sqlite3
import unittest

from src.config.settings import SOURCE_DB_PATH, WAREHOUSE_DB_PATH
from src.models.raw.raw_tables import EXPECTED_SCHEMAS
from tests.utils import ensure_warehouse_ready



def quote_columns(columns: list[str]) -> list[str]:
  return [f'"{column}"' for column in columns]



class TetsRawFidelity(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    ensure_warehouse_ready()
  
  def test_raw_tables_match_source(self) -> None:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)
    try:
      con.execute(f"ATTACH DATABASE '{SOURCE_DB_PATH}' AS source;")

      for table, columns in EXPECTED_SCHEMAS.items():
        raw_table = f"raw_{table}"
        with self.subTest(table=table):
          cursor = con.execute(f"PRAGMA table_info({raw_table});")
          raw_columns = [row[1] for row in cursor.fetchall()]
          self.assertEqual(raw_columns, columns)

          source_count = con.execute(
            f"SELECT COUNT(*) FROM source.{table};"
          ).fetchone()[0]
          raw_count = con.execute(
            f"SELECT COUNT(*) FROM {raw_table};"
          ).fetchone()[0]
          self.assertEqual(raw_count, source_count)

          quoted_columns = quote_columns(columns)
          cast_columns = ", ".join(
            [f"CAST({column} AS TEXT) AS {column}" for column in quoted_columns]
          )
          select_raw = ", ".join(quoted_columns)

          diff_source = con.execute(
            f"""
            SELECT COUNT(*) FROM (
              SELECT {cast_columns} FROM source.{table}
              EXCEPT
              SELECT {select_raw} FROM {raw_table}
            )
            """
          ).fetchone()[0]
          diff_raw = con.execute(
            f"""
            SELECT COUNT(*) FROM (
              SELECT {select_raw} FROM {raw_table}
              EXCEPT
              SELECT {cast_columns} FROM source.{table}
            )
            """
          ).fetchone()[0]

          self.assertEqual(diff_source, 0)
          self.assertEqual(diff_raw, 0)

    finally:
      con.close()



if __name__ == '__main__':
  unittest.main()