DROP TABLE IF EXISTS stg_coaches;

CREATE TABLE stg_coaches AS
SELECT
  coach_id,
  NULLIF(TRIM(name), '') AS name,
  team_id,
  NULLIF(TRIM(nationality), '') AS nationality
FROM raw_coaches