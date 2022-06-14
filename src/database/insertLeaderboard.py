import sqlite3

conn = sqlite3.connect('src/data/db.sqlite')
cur = conn.cursor()


def insertLeaderboard(username, result, difficulty):
    cur.execute("""SELECT rowid FROM ACCOUNTS WHERE username = ?""", (username,))

    data = cur.fetchone()

    if data is None:
        print("No user logged in")
    else:
        cur.execute("""INSERT INTO GAMES (user_id, result, difficulty) VALUES (?,?,?)""",
                    (data[0], result, difficulty,))

        conn.commit()
        print("Done")
