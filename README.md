# Football Data European Top 5 Leagues

An end-to-end ELT pipeline that loads football data from a SQLite source database, stages and transforms it with SQL, and builds analytical marts for the European top five leagues. The pipeline is orchestrated in Python and writes to a separate SQLite warehouse.

## Overview

The pipeline follows a simple ELT flow:

1. **Extract**: Read all tables from the source SQLite database.
2. **Load**: Create `raw_` tables in the warehouse, insert data, and validate the load.
3. **Transform**: Execute staging and mart SQL models to curate analytics-ready tables.

## Project Structure

```
.
├── data/
│   ├── source/                 # Source SQLite database
│   └── warehouse/              # Warehouse SQLite database
├── src/
│   ├── config/                 # Configuration constants
│   ├── extract/                # Source extraction utilities
│   ├── load/                   # Warehouse initialization + raw load
│   ├── transform/              # SQL-based staging/mart transforms
│   └── utils/                  # Logging and DB helpers
├── main.py                     # Pipeline entrypoint
└── requirements.txt
```

## Data Sources & Outputs

- **Source DB**: `data/source/sports_league.sqlite`
- **Warehouse DB**: `data/warehouse/football_dw.sqlite`

### Raw Layer

Each source table is copied into the warehouse as `raw_<table_name>` with lightweight validations:

- Row count matches the source.
- Column count matches the source.
- Table is not empty.

### Staging Models

Staging models clean and type cast raw data. They live in `src/transform/sql/staging/` and include:

- `stg_leagues`
- `stg_seasons`
- `stg_matches`
- `stg_scores`
- `stg_players`
- `stg_teams`
- `stg_stadiums`
- `stg_coaches`
- `stg_referees`
- `stg_standings`

### Mart Models

Mart models provide analytics-ready tables. Current marts live in `src/transform/sql/marts/`:

- `mrt_team_performance` (sample league and team performance metrics)

## Running the Pipeline

1. Ensure you have Python available.
2. Run the pipeline:

```bash
python main.py
```

The run initializes the warehouse, loads raw data, and executes all staging and mart SQL models.

## Configuration

Configuration is located in `src/config/settings.py`:

- `SOURCE_DB_PATH`: location of the source database
- `WAREHOUSE_DB_PATH`: location of the warehouse database
- `SQL_STAGING_FILES_PATH`: directory with staging SQL models
- `SQL_MARTS_FILES_PATH`: directory with mart SQL models

Update these paths if you move the databases or SQL directories.

## Notes

- The pipeline is idempotent: raw tables are dropped and rebuilt on each run.
- Staging and mart models are executed in filename order.
