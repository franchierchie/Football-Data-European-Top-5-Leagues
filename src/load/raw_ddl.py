import sqlite3

# Data Definition Language
def create_raw_tables(
  cursor: sqlite3.Cursor,
  raw_table_name: str,
  columns: list[str]
) -> None:
  column_defs = ', '.join([f'"{col}" TEXT' for col in columns])

  create_sql = f"""
  CREATE TABLE IF NOT EXISTS {raw_table_name} (
    {column_defs}
  );
  """

  cursor.execute(create_sql)