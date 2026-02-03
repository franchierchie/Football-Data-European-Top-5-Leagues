DROP TABLE IF EXISTS stg_matches;

CREATE TABLE stg_matches AS
SELECT
  match_id,
  season_id,
  league_id,
  DATE(NULLIF(matchday, '')) AS matchday,
  home_team_id,
  away_team_id,
  NULLIF(TRIM(winner), '') AS winner,
  DATE(NULLIF(utc_date, '')) AS utc_date
FROM raw_matches