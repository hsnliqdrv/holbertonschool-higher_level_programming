-- List all genres of the show 'Dexter'
SELECT g.name FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg ON sg.genre_id = g.id
LEFT JOIN tv_shows AS s ON sg.show_id = s.id
WHERE s.title = 'Dexter' ORDER BY g.name;
