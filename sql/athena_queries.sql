-- ============================================================
-- AWS NBA Analytics Pipeline
-- Athena Queries
-- ============================================================

-- Join game metadata with team-level game statistics.
-- The game_id field connects the game_info and game tables.

SELECT
    a.game_id,
    a.game_date,
    b.*
FROM "nba-database-json"."game_info" AS a
JOIN "nba-database-json"."game" AS b
    ON a.game_id = b.game_id;
