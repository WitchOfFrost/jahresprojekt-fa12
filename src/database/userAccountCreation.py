import hashlib
import bcrypt
import base64
import sqlite3
import re

from getpass import getpass

conn = sqlite3.connect('data/db.sqlite')

cur = ''
cur = conn.cursor()


def getInput():
    username = str(input("Enter a Username > "))
    password = str(getpass("Enter a Password [HIDDEN] > "))

    validityCheck(username, password)


def validityCheck(username, password):
    cur.execute("SELECT rowid FROM ACCOUNTS WHERE username = ?", (username,))
    data = cur.fetchone()
    if data is None:
        print('There is no entry for %s' % username)

        if (6 <= len(password) <= 16 and 6 <= len(username) <= 16):

            pwd = hashing(password)

            if pwd == False:
                    print("Failed to hash password, please try again!")
                    getInput()
                    return

            else:
                insertUser(username, pwd)
        else:
            print(
                    "Username and Password have to be between 6 and 16 Characters!")
            getInput()
            return
    else:
        print('Found username %s in Database at row %s' % (username, data[0]))


def insertUser(username, password):
    cur.execute("INSERT INTO ACCOUNTS (username, password) VALUES (?,?)",
                (username, password))
    conn.commit()
    print("Added User to Database")


def hashing(password):
    sha256 = hashlib.sha256(password.encode())
    base64_pw = base64.b64encode(sha256.hexdigest().encode())
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(base64_pw, salt)

    if bcrypt.checkpw(base64_pw, hashed):
        print("Valid Password")
        return hashed
    else:
        print("Invalid Password")
        return False


getInput()
