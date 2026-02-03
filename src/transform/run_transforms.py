import sqlite3
from pathlib import Path

from src.utils.logging import logging
from src.config.settings import SQL_STAGING_FILES_PATH, SQL_MARTS_FILES_PATH
from src.utils.db import get_warehouse_connection

logger = logging.getLogger(__name__)

STAGING_DIR = Path(SQL_STAGING_FILES_PATH)
MARTS_DIR = Path(SQL_MARTS_FILES_PATH)



def run_layer(sql_files, con, cursor, mode):
  for sql_file in sql_files:
    logger.info(f"Running {mode} model: %s", sql_file.name)
    
    try:
      sql = sql_file.read_text(encoding='utf-8')
      cursor.executescript(sql)
      con.commit()
      logger.info("Completed: %s", sql_file.name)
    
    except Exception:
      logger.exception(f"Failed {mode} model: %s", sql_file.name)
      con.rollback()
      raise



def run_staging_transforms(con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
  sql_files = sorted(STAGING_DIR.glob("*.sql"))

  if not sql_files:
    raise RuntimeError('No staging SQL files found')
  
  run_layer(sql_files=sql_files, con=con, cursor=cursor, mode="staging")



def run_mart_transforms(con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
  sql_files = sorted(MARTS_DIR.glob("*.sql"))

  if not sql_files:
    raise RuntimeError('No mart SQL files found')

  run_layer(sql_files=sql_files, con=con, cursor=cursor, mode="mart")




def run_transforms():
  con = get_warehouse_connection()
  cursor = con.cursor()

  run_staging_transforms(con=con, cursor=cursor)
  run_mart_transforms(con=con, cursor=cursor)

  cursor.close()
  con.close()