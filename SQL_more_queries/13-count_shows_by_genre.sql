-- List all genres and displays number of shows
SELECT tv_genres.name AS genre,
       COUNT(sg.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres AS sg ON tv_genres.id = sg.genre_id
GROUP BY tv_genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
