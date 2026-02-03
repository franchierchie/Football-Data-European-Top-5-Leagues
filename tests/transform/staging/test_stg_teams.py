import sqlite3
import unittest

from src.config.settings import WAREHOUSE_DB_PATH
from src.models.source.teams import EXPECTED_COLUMNS
from tests.utils import ensure_warehouse_ready, count_empty_strings, count_invalid_type



class TestStgTeams(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    ensure_warehouse_ready()
  
  def test_stg_teams_structure(self) -> None:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)
    try:
      cursor = con.execute("PRAGMA table_info(stg_teams);")
      actual_columns = [row[1] for row in cursor.fetchall()]
      self.assertEqual(actual_columns, EXPECTED_COLUMNS)

      self.assertEqual(count_empty_strings(con, "stg_teams", "name"), 0)
      self.assertEqual(count_empty_strings(con, "stg_teams", "cresturl"), 0)
      self.assertEqual(count_invalid_type(con, "stg_teams", "founded_year", "integer"), 0)

    finally:
      con.close()



if __name__ == "__main__":
  unittest.main()