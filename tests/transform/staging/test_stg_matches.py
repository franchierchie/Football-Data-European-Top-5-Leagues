import unittest
import sqlite3

from src.config.settings import WAREHOUSE_DB_PATH
from src.models.source.matches import EXPECTED_COLUMNS
from tests.utils import ensure_warehouse_ready, count_empty_strings, count_invalid_date_strings



class TestStgMatches(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    ensure_warehouse_ready()
  
  def test_stg_matches_structure(self) -> None:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)
    try:
      cursor = con.execute("PRAGMA table_info(stg_matches);")
      actual_columns = [row[1] for row in cursor.fetchall()]
      self.assertEqual(actual_columns, EXPECTED_COLUMNS)

      self.assertEqual(count_empty_strings(con, "stg_matches", "winner"), 0)
      self.assertEqual(count_invalid_date_strings(con, "stg_matches", "matchday"), 0)
      self.assertEqual(count_invalid_date_strings(con, "stg_matches", "utc_date"), 0)

    finally:
      con.close()



if __name__ == '__main__':
  unittest.main()