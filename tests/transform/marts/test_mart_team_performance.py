import sqlite3
import unittest
from pathlib import Path

from src.config.settings import WAREHOUSE_DB_PATH, MART_PATH
from src.models.marts.team_performance import EXPECTED_COLUMNS
from tests.utils import ensure_warehouse_ready



class TestMartTeamPerformance(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    ensure_warehouse_ready
  
  def test_mart_team_performance_query(self) -> None:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)
    try:
      sql_path = Path(f"{MART_PATH}mrt_team_performance.sql")
      sql = sql_path.read_text(encoding="utf-8")

      cursor = con.execute(sql)
      rows = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]

      self.assertEqual(columns, EXPECTED_COLUMNS)
      self.assertGreater(len(rows), 0)

      for row in rows:
        row_data = dict(zip(columns, row))
        self.assertIsNotNone(row_data["team_id"])
        self.assertTrue(row_data["name"])
        self.assertTrue(row_data["league"])
        self.assertIsNotNone(row_data["points"])

        goals_scored = row_data["goals_scored"]
        goals_conceded = row_data["goals_conceded"]
        goal_difference = row_data["goal_difference"]
        if goals_scored is not None and goals_conceded is not None:
          self.assertEqual(goal_difference, goals_scored - goals_conceded)

    finally:
      con.close()



if __name__ == '__main__':
  unittest.main()