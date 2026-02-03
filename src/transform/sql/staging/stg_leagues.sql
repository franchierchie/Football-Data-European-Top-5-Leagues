DROP TABLE IF EXISTS stg_leagues;

CREATE TABLE stg_leagues AS
SELECT
  league_id,
  NULLIF(TRIM(name), '') AS name,
  NULLIF(TRIM(country), '') AS country,
  country_id,
  NULLIF(TRIM(icon_url), '') AS icon_url,
  CAST(NULLIF(cl_spot, '') AS INTEGER) AS cl_spot,
  CAST(NULLIF(uel_spot, '') AS INTEGER) AS uel_spot,
  CAST(NULLIF(relegation_spot, '') AS INTEGER) AS relegation_spot
FROM raw_leagues