DROP TABLE IF EXISTS stg_standings;

CREATE TABLE stg_standings AS
SELECT
  standing_id,
  season_id,
  league_id,
  CAST(NULLIF(position, '') AS INTEGER) AS position,
  team_id,
  CAST(NULLIF(played_games, '') AS INTEGER) AS played_games,
  CAST(NULLIF(won, '') AS INTEGER) AS won,
  CAST(NULLIF(draw, '') AS INTEGER) AS draw,
  CAST(NULLIF(lost, '') AS INTEGER) AS lost,
  CAST(NULLIF(points, '') AS INTEGER) AS points,
  CAST(NULLIF(goals_for, '') AS INTEGER) AS goals_for,
  CAST(NULLIF(goals_against, '') AS INTEGER) AS goals_against,
  CAST(NULLIF(goal_difference, '') AS INTEGER) AS goal_difference,
  form
FROM raw_standings