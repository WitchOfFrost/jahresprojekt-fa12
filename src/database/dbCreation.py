import sqlite3

def createDB():
	conn = sqlite3.connect('src/data/db.sqlite')

	conn.execute("""CREATE TABLE IF NOT EXISTS "ACCOUNTS" (
		"username"	TEXT NOT NULL UNIQUE,
		"password"	TEXT NOT NULL,
		"email"	TEXT UNIQUE
    	)""")

	conn.execute("""CREATE TABLE IF NOT EXISTS "GAMES" (
		"user_id"	INTEGER NOT NULL,
		"result"	INTEGER NOT NULL,
		"difficulty"	INTEGER NOT NULL,
		"savegame"	BLOB
    	)""")
