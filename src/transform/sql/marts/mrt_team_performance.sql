SELECT t.team_id, name, league, position, played_games, won, draw, lost, goals_scored, goals_conceded, goal_difference, points FROM stg_teams AS t
JOIN (
  SELECT league_id, position, team_id, played_games, won, draw, lost, points FROM stg_standings
) AS st ON t.team_id = st.team_id
JOIN (
  SELECT league_id, name AS league FROM stg_leagues
) as l ON st.league_id = l.league_id
JOIN (
  SELECT team_id,
    SUM(home_goals + away_goals) AS goals_scored,
    SUM(home_conceded + away_conceded) AS goals_conceded,
    SUM(home_goals + away_goals) - SUM(home_conceded + away_conceded) AS goal_difference
  FROM (
    SELECT home_team_id AS team_id,
      full_time_home AS home_goals,
      full_time_away AS home_conceded,
      0 AS away_goals,
      0 AS away_conceded
    FROM (
      SELECT m.match_id, home_team_id, away_team_id, full_time_home, full_time_away
      FROM stg_matches AS m
      JOIN (
        SELECT match_id, full_time_home, full_time_away FROM stg_scores
      ) AS sc ON m.match_id = sc.match_id
    )

    UNION ALL

    SELECT away_team_id AS team_id,
      0 AS home_goals,
      0 AS home_conceded,
      full_time_away AS away_goals,
      full_time_home AS away_conceded
    FROM (
      SELECT m.match_id, home_team_id, away_team_id, full_time_home, full_time_away
      FROM stg_matches AS m
      JOIN (
        SELECT match_id, full_time_home, full_time_away FROM stg_scores
      ) AS sc ON m.match_id = sc.match_id
    )
  ) GROUP BY team_id
) as gs_gc ON t.team_id = gs_gc.team_id;