import sqlite3
import unittest

from src.config.settings import WAREHOUSE_DB_PATH
from src.models.source.standings import EXPECTED_COLUMNS, INTEGER_COLUMNS
from tests.utils import ensure_warehouse_ready, count_invalid_type



class TestStgStandings(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    ensure_warehouse_ready()
  
  def test_stg_standings_structure(self) -> None:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)

    try:
      cursor = con.execute("PRAGMA table_info(stg_standings);")
      actual_columns = [row[1] for row in cursor.fetchall()]
      self.assertEqual(actual_columns, EXPECTED_COLUMNS)

      for column in INTEGER_COLUMNS:
        with self.subTest(column=column):
          self.assertEqual(count_invalid_type(con, "stg_standings", column, "integer"), 0)

    finally:
      con.close()



if __name__ == '__main__':
  unittest.main()