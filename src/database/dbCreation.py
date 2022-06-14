import sqlite3


def createDB(debug):

	if(debug == True):
		path = input("Input Database Path")
	else:
		path = 'data/db.sqlite'

	conn = sqlite3.connect(path)

	conn.execute("""CREATE TABLE IF NOT EXISTS "ACCOUNTS" (
		"username"	TEXT NOT NULL UNIQUE,
		"password"	TEXT NOT NULL,
		"email"	TEXT NOT NULL UNIQUE
    	)""")

	conn.execute("""CREATE TABLE IF NOT EXISTS "GAMES" (
		"user_id"	INTEGER NOT NULL,
		"result"	INTEGER NOT NULL,
		"difficulty"	INTEGER NOT NULL,
		"savegame"	BLOB
    	)""")
