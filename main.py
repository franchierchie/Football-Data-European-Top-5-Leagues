import logging

from src.utils.logging import setup_logging
from src.load.init_warehouse import init_warehouse
from src.extract.read_source import extract_tables
from src.load.load_raw_tables import load_raw_tables
from src.transform.run_transforms import run_transforms

logger = logging.getLogger(__name__)

if __name__ == '__main__':
  setup_logging()
  logger.info("Pipeline started")
  
  logger.info("Initializing warehouse")
  init_warehouse()
  logger.info("Warehouse ready")

  # Extract
  logger.info("Extracting source metadata and data")
  extracted_raw_tables = extract_tables()
  logger.info("Extraction completed: %d tables", len(extracted_raw_tables))

  # Load
  logger.info("Loading raw tables")
  load_raw_tables(extracted_raw_tables)
  logger.info("Raw load completed")

  # Transform
  run_transforms()

  logger.info("ELT pipeline finished successfully")