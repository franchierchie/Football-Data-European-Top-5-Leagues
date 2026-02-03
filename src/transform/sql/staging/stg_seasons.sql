DROP TABLE IF EXISTS stg_seasons;

CREATE TABLE stg_seasons AS
SELECT
  season_id,
  league_id,
  NULLIF(TRIM(year), '') AS year
FROM raw_seasons