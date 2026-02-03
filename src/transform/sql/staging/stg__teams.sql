DROP TABLE IF EXISTS stg_teams;

CREATE TABLE stg_teams AS
SELECT
  team_id,
  NULLIF(TRIM(name), '') AS name,
  CAST(NULLIF(founded_year, '') AS INTEGER) AS founded_year,
  stadium_id,
  league_id,
  coach_id,
  NULLIF(TRIM(cresturl), '') AS cresturl
FROM raw_teams