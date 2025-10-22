-- List all records of table second_table
-- Dont list rows where name is null
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
