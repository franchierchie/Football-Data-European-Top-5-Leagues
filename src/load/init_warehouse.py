from pathlib import Path

from src.config.settings import WAREHOUSE_DB_FOLDER_PATH
from src.utils.db import get_warehouse_connection

directory_path = Path(WAREHOUSE_DB_FOLDER_PATH)

def init_warehouse():
  # data/warehouse/football_dw.sqlite

  if not directory_path.is_dir():
    directory_path.mkdir(parents=True, exist_ok=True)
  
  con = get_warehouse_connection()
  con.close()