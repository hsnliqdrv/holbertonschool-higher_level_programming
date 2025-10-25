#!/usr/bin/python3
"""5-filter_cities

Select all cities of a state from database on localhost:3306
Accepts username, password, database and keyword as argv
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT c.name FROM cities AS c
        LEFT JOIN states AS s ON c.state_id=s.id
        WHERE BINARY s.name = %s
        ORDER BY c.id ASC""", (argv[4],)
    )
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
