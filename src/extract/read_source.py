from src.utils.db import get_source_connection

def extract_tables() -> dict:
  # Connect to the source
  con = get_source_connection()
  cursor = con.cursor()

  # Get table names
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  table_names = cursor.fetchall()

  tables = {}

  # Loop over the table names and get thier respective rows
  for table in table_names:
    cursor.execute(f"SELECT * FROM {table[0]};")
    table_rows = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({table[0]});")
    table_columns = [col[1] for col in cursor.fetchall()]

    tables[table[0]] = {
      "columns": table_columns,
      "rows": table_rows
    }
  
  cursor.close()
  con.close()

  return tables