import sqlite3 as sql

DB_NAME = 'test_database'


db = sql.connect(DB_NAME)
cursor = db.cursor()
cursor.execute("CREATE TABLE users (id int PRIMARY_KEY, name varchar(20))")

