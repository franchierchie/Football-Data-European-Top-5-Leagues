import sqlite3

# Data Manipulation Language
def insert_raw_rows(
  cursor: sqlite3.Cursor,
  raw_table_name: str,
  columns: list[str],
  rows: list[tuple]
) -> None:
  placeholders = ', '.join(['?'] * len(columns))
  column_defs = ', '.join([f'{col}' for col in columns])

  insert_sql = f"""
  INSERT INTO {raw_table_name} ({column_defs})
  VALUES ({placeholders});
  """

  cursor.executemany(insert_sql, rows)