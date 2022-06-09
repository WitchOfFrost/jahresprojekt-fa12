import hashlib
import bcrypt
import base64
import sqlite3
import re

from getpass import getpass

conn = sqlite3.connect('data/db.sqlite')

# UNUSED


def selectDatabase(debug):
    if(debug == True):
        conn = sqlite3.connect(input("Input Database Path"))
    else:
        conn = sqlite3.connect('data/db.sqlite')


cur = ''
cur = conn.cursor()


def getInput():
    username = str(input("Enter a Username > "))
    password = str(getpass("Enter a Password [HIDDEN] > "))
    password_check = str(getpass("Enter the same Password again [HIDDEN] > "))
    email = str(input("Enter an Email > "))

    if (password != password_check):
        print("Password does not match. Please try again!")
        getInput()
    else:
        validityCheck(username, password, email)


def validityCheck(username, password, email):
    cur.execute("SELECT rowid FROM ACCOUNTS WHERE username = ?", (username,))
    data = cur.fetchone()
    if data is None:
        print('There is no entry for %s' % username)

        cur.execute("SELECT rowid FROM ACCOUNTS WHERE email = ?", (email,))
        data = cur.fetchone()
        if data is None:
            print('There is no entry for %s' % email)

            if re.search('^[a-zA-Z0-9_!#$%&’*+/=?`{|}~^.-]+@[a-zA-Z0-9.-]+$', email):
                if (6 <= len(password) <= 32 and 6 <= len(username) <= 32):

                    pwd = hashing(password)

                    if pwd == False:
                        print("Failed to hash password, please try again!")
                        getInput()
                        return

                    else:
                        insertUser(username, pwd, email)
                else:
                    print(
                        "Username and Password have to be between 6 and 32 Characters!")
                    getInput()
                    return
            else:
                print("Invalid Email!")
                getInput()
                return
        else:
            print('Found username %s in Database at row %s' % (email, data[0]))
    else:
        print('Found username %s in Database at row %s' % (username, data[0]))


def insertUser(username, password, email):
    cur.execute("INSERT INTO ACCOUNTS (username, password, email) VALUES (?,?,?)",
                (username, str(password), email))
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
