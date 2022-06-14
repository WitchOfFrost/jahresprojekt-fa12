import hashlib
import bcrypt
import base64
import sqlite3

from getpass import getpass

conn = sqlite3.connect('src/data/db.sqlite')

cur = conn.cursor()


def getInput():
    username = str(input("Enter a Username > "))
    password = str(getpass("Enter a Password > "))

    validityCheck(username, password)


def validityCheck(username, password):
    cur.execute("SELECT username, password FROM ACCOUNTS WHERE username = ? LIMIT 1", (username,))
    data = cur.fetchone()
    
    if bcrypt.checkpw(password.encode(), data[1]):
        print("Failed")
        return False
    else:
        print("Valid")
        return True

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
