# SQL - More Queries

## Description
This project covers advanced MySQL concepts including user management, privileges, constraints, and multi-table queries.

## Learning Objectives
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- The length of files will be tested using `wc`

## Comment format
```sql
-- Description of what the query does
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Author
Ian Aviles