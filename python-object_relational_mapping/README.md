# Python - Object Relational Mapping

This project covers how to connect a Python script to a MySQL database,
first using the low-level `MySQLdb` module, then using the `SQLAlchemy`
ORM to map Python classes to MySQL tables.

## General

### How to connect to a MySQL database from a Python script

A connection is the object representing an open link between the
Python process and the MySQL server. Nothing can be queried until one
exists. With `MySQLdb`, it's created by calling `MySQLdb.connect()`
with the server's host/port and login credentials:

```python
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa"
)
```

* `host` / `port` say which server to talk to — `localhost:3306` is
  the default for a MySQL server running on the same machine.
* `user` / `passwd` are the MySQL credentials (passed in as script
  arguments in this project, e.g. `sys.argv[1]` and `sys.argv[2]`).
* `db` is the specific database on that server to connect to.

Once open, a **cursor** is created from the connection
(`db.cursor()`). The cursor is what actually sends SQL statements to
the server and reads back results. Both should be explicitly closed
with `cur.close()` and `db.close()` when the script is done.

### How to SELECT rows in a MySQL table from a Python script

`SELECT` is read-only, so the flow is: execute the query, then pull
results out of the cursor.

```python
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()
```

* `cur.execute(query)` sends the SQL string to the server.
* `cur.fetchall()` returns every matching row as a list of tuples —
  one tuple per row, in column order.
* `cur.fetchone()` is the alternative when only one row (or one row at
  a time) is needed instead of the full result set.
* No `db.commit()` is needed for a `SELECT`, since nothing changes in
  the database — commit only matters for writes.

### How to INSERT rows in a MySQL table from a Python script

`INSERT` changes the data in the table, so it needs one extra step
compared to `SELECT`: committing the transaction.

```python
cur = db.cursor()
cur.execute("INSERT INTO states (name) VALUES (%s)", ("Louisiana",))
db.commit()
cur.close()
db.close()
```

* `cur.execute(query, params)` — passing values as a second tuple
  argument (instead of building the query string with an f-string or
  `.format()`) lets the driver escape them safely and avoids SQL
  injection. The `%s` is a placeholder the driver fills in, not Python
  string formatting.
* `db.commit()` is what actually saves the change. Without it, the
  insert can be rolled back silently when the connection closes, and
  the row never persists.

### What ORM means

ORM stands for **Object-Relational Mapping**. It's a technique (and
usually a library) for working with a database through Python classes
and objects instead of writing raw SQL strings by hand. It bridges two
different ways of modeling data:

* Relational databases store data in tables, rows, and columns.
* Object-oriented code models data as classes, instances, and
  attributes.

An ORM maps between the two: a table becomes a class, a row becomes an
instance of that class, and a column becomes an attribute on that
instance. Instead of writing
`SELECT * FROM states WHERE name = "California"`, you'd write
something like `session.query(State).filter_by(name="California")`.
`SQLAlchemy` is the ORM used in this project, and calling its raw
`execute()` isn't allowed here — the point is to work through the
ORM's own query interface instead.

### How to map a Python Class to a MySQL table

With SQLAlchemy's declarative base, a class describes a table's
structure directly in Python — this is the actual "mapping":

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in the states table."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
```

* `Base = declarative_base()` creates a base class that keeps track of
  all mapped classes and their tables.
* `__tablename__` is the required attribute naming the actual MySQL
  table this class corresponds to.
* Each `Column(...)` attribute maps one column of that table — its
  type (`Integer`, `String(256)`, etc.) and constraints
  (`primary_key`, `nullable`) mirror what you'd otherwise write in a
  `CREATE TABLE` statement.
* Once mapped, creating a `State(name="Ohio")` instance and adding it
  to a session behaves like inserting a row; querying `State` objects
  through the session behaves like a `SELECT` — all without writing
  SQL directly.

## Notes for this project

* Every script starts with `#!/usr/bin/python3` and must be executable
  (`chmod +x`).
* Scripts take command-line arguments for MySQL username, password, and
  database name, in that order.
* Since I'm on Windows using WSL, execute permission has to be set with
  `git update-index --chmod=+x <file>` before committing so the Linux
  test system sees the correct file permissions.
* Every module, class, and function needs a real docstring explaining
  its purpose, not just a placeholder.

## Author

Ian Aviles