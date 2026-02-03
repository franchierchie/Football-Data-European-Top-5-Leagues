DROP TABLE IF EXISTS stg_referees;

CREATE TABLE stg_referees AS
SELECT
  referee_id,
  NULLIF(TRIM(name), '') AS name,
  NULLIF(TRIM(nationality), '') AS nationality
FROM raw_referees