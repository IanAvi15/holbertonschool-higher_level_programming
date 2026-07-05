#!/usr/bin/python3
"""Script that safely displays all states whose name matches
the given argument, in the hbtn_0e_0_usa database.
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
    # Create a cursor and safely pass the user's search term as a
    # parameter, instead of building the query string directly
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    # Print each row as a tuple
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
