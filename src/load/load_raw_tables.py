import sqlite3

from src.utils.db import get_warehouse_connection
from src.load.raw_ddl import create_raw_tables
from src.load.raw_dml import insert_raw_rows
from src.load.raw_validations import validate_row_count, validate_column_count, validate_not_empty

def load_raw_tables(extracted_raw_tables: dict):
  con = get_warehouse_connection()
  cursor = con.cursor()

  try:
    for table, payload in extracted_raw_tables.items():
      raw_name = f"raw_{table}"

      cursor.execute(f"DROP TABLE IF EXISTS raw_{table};")

      create_raw_tables(
        cursor=cursor,
        raw_table_name=raw_name,
        columns=payload['columns']
      )

      insert_raw_rows(
        cursor=cursor,
        raw_table_name=raw_name,
        columns=payload['columns'],
        rows=payload['rows']
      )

      con.commit()

      validate_row_count(
        cursor=cursor,
        raw_table_name=raw_name,
        expected_count=len(payload['rows'])
      )

      validate_column_count(
        cursor=cursor,
        raw_table_name=raw_name,
        expected_columns=len(payload['columns'])
      )

      validate_not_empty(
        cursor=cursor,
        raw_table_name=raw_name
      )

  except Exception:
    con.rollback()
    raise

  finally:  
    cursor.close()
    con.close()