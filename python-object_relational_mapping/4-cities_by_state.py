#!/usr/bin/python3
"""Script that lists all cities along with their state name,
from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL server using the given username, password,
    # and database name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create a cursor and execute a single query joining cities
    # and states, sorted by cities.id
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    # Print each row as a tuple
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
