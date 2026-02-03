DROP TABLE IF EXISTS stg_stadiums;

CREATE TABLE stg_stadiums AS
SELECT
  stadium_id,
  NULLIF(TRIM(name), '') AS name,
  NULLIF(TRIM(location), '') AS location,
  CAST(NULLIF(capacity, '') AS INTEGER) AS capacity
FROM raw_stadiums