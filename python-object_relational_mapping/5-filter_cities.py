#!/usr/bin/python3
"""Script that lists all cities of a given state, safely from
user input, in the database hbtn_0e_4_usa.
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
    # Create a cursor and safely execute a single query joining
    # cities and states, filtering on the given state name
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name "
        "FROM cities INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    # Collect all city names and print them comma-separated
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    db.close()
