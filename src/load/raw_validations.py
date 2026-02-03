import sqlite3

def validate_row_count(
  cursor: sqlite3.Cursor,
  raw_table_name: str,
  expected_count: int
) -> None:
  cursor.execute(f"SELECT COUNT(*) FROM {raw_table_name};")
  actual_count = cursor.fetchall()[0][0]

  if actual_count != expected_count:
    raise RuntimeError(
      f"Row count mismatch for {raw_table_name}: "
      f"expected {expected_count}, got {actual_count}"
    )

def validate_column_count(
  cursor: sqlite3.Cursor,
  raw_table_name: str,
  expected_columns: int
) -> None:
  cursor.execute(f"PRAGMA table_info({raw_table_name});")
  actual_columns = len(cursor.fetchall())

  if actual_columns != expected_columns:
    raise RuntimeError(
      f"Column count mismatch for {raw_table_name}: "
      f"expected {expected_columns}, got {actual_columns}"
    )

def validate_not_empty(
  cursor: sqlite3.Cursor,
  raw_table_name: str,
) -> None:
  cursor.execute(f"SELECT 1 FROM {raw_table_name} LIMIT 1;")
  if cursor.fetchone() is None:
    raise RuntimeError(
      f"Raw table {raw_table_name} is empty"
    )