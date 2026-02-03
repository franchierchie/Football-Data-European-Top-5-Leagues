import sqlite3

from src.config.settings import SOURCE_DB_PATH, WAREHOUSE_DB_PATH

def get_source_connection():
  try:
    con = sqlite3.connect(SOURCE_DB_PATH)
    return con

  except sqlite3.Error as error:
    raise RuntimeError('Error occured -', error) from error

def get_warehouse_connection():
  try:
    con = sqlite3.connect(WAREHOUSE_DB_PATH)
    return con

  except sqlite3.Error as error:
    raise RuntimeError('Error occured -', error) from error