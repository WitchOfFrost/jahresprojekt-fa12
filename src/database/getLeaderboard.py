import sqlite3

conn = sqlite3.connect('src/data/db.sqlite')


def getData():
    cur = conn.cursor()

    cur.execute("""SELECT GAMES.user_id, SUM((SELECT GAMES.result + GAMES.difficulty WHERE GAMES.result = 1)) AS points, ACCOUNTS.username FROM GAMES INNER JOIN ACCOUNTS ON GAMES.user_id = ACCOUNTS.rowid GROUP BY user_id ORDER BY points DESC LIMIT 12""")

    data = cur.fetchall()

    returnData = []

    for row in data:
        returnData.append(row)

    cur.close()
    return returnData
