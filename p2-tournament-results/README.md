## Project 2: Tournament Results

In Project 2 will be using a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

This project has two parts: defining the database schema (SQL table definitions) in tournament.sql, and writing code that will use it to track a Swiss tournament in tournament.py.

#### Files
- tournament.sql  - this file is used to set up database schema.
- tournament.py - this file is used to provide access to the database via a library of functions which can add, delete or query data in the database to another python program (a client program). 
- tournament_extra_test.py - this is a client program (this file was changed slightly to accommodate some of the extra credit functionality) which will use the functions written in the tournament.py module.

#### Run Instructions

Navigate to the project folder and run the following code:
- Create database: `psql -f tournament.sql`
- Execute test file: `python tournament_extra_test.py`
