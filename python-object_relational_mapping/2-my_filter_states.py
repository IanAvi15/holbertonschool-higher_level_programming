#!/usr/bin/python3
"""Script that displays all states whose name matches
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
    # Create a cursor and build the query using the user's search term
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cur.execute(query)
    # Print each row as a tuple
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
