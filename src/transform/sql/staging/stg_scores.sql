DROP TABLE IF EXISTS stg_scores;

CREATE TABLE stg_scores AS
SELECT
  score_id,
  match_id,
  CAST(NULLIF(full_time_home, '') AS INTEGER) AS full_time_home,
  CAST(NULLIF(full_time_away, '') AS INTEGER) AS full_time_away,
  CAST(NULLIF(half_time_home, '') AS INTEGER) AS half_time_home,
  CAST(NULLIF(half_time_away, '') AS INTEGER) AS half_time_away
FROM raw_scores