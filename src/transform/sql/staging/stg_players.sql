DROP TABLE IF EXISTS stg_players;

CREATE TABLE stg_players AS
SELECT
  player_id,
  team_id,
  NULLIF(TRIM(name), '') AS name,
  CAST(NULLIF(position, '') AS INTEGER) AS position,
  DATE(NULLIF(date_of_birth, '')) AS date_of_birth,
  NULLIF(TRIM(nationality), '') AS nationality
FROM raw_players