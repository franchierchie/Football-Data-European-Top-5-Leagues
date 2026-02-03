TABLE = "standings"

REQUIRED_COLUMNS = {
  "league_id": "TEXT",
  "position": "INTEGER",
  "team_id": "TEXT",
  "played_games": "INTEGER",
  "won": "INTEGER",
  "draw": "INTEGER",
  "lost": "INTEGER",
  "points": "INTEGER"
}

OPTIONAL_COLUMNS = {
  "standing_id": "TEXT",
  "season_id": "TEXT",
  "goals_for": "INTEGER",
  "goals_against": "INTEGER",
  "goals_difference": "INTEGER",
  "form": "TEXT"
}