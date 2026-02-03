from __future__ import annotations

import sqlite3

from src.extract.read_source import extract_tables
from src.load.init_warehouse import init_warehouse
from src.load.load_raw_tables import load_raw_tables
from src.transform.run_transforms import run_transforms

WAREHOUSE_READY = False

def ensure_warehouse_ready() -> None:
  global WAREHOUSE_READY
  if WAREHOUSE_READY:
    return

  init_warehouse()
  extracted_tables = extract_tables()
  load_raw_tables(extracted_tables)
  run_transforms()
  WAREHOUSE_READY = True



def count_invalid_type(
  con: sqlite3.Connection,
  table: str,
  column: str,
  expected_type: str
) -> int:
  cursor = con.execute(
    f"""
    SELECT COUNT(*) FROM {table}
    WHERE {column} IS NOT NULL
      AND typeof({column}) != '{expected_type}';
    """
  )
  return cursor.fetchone()[0]



def count_empty_strings(
  con: sqlite3.Connection,
  table: str,
  column: str
) -> int:
  cursor = con.execute(
    f"""
    SELECT COUNT(*) FROM {table}
    WHERE {column} = '';
    """
  )
  return cursor.fetchone()[0]



def count_invalid_date_strings(
  con: sqlite3.Connection,
  table: str,
  column: str
) -> int:
  cursor = con.execute(
    f"""
    SELECT COUNT(*) FROM {table}
    WHERE {column} IS NOT NULL
      AND {column} NOT GLOB '????-??-??'
      AND {column} NOT GLOB '-????-??-??';
    """
  )
  return cursor.fetchone()[0]