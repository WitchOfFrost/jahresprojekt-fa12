import hashlib
import bcrypt
import base64
import sqlite3
import re

from getpass import getpass

conn = sqlite3.connect('data/db.sqlite')

def selectDatabase(debug):
    # UNUSED
    if(debug == True):
        conn = sqlite3.connect(input("Input Database Path"))
    else:
        conn = sqlite3.connect('data/db.sqlite')


cur = ''
cur = conn.cursor()


def getInput():
    username = str(input("Enter a Username > "))
    password = str(getpass("Enter a Password [HIDDEN] > "))
    #password_check = str(getpass("Enter the same Password again [HIDDEN] > "))
    #email = str(input("Enter an Email > "))

    validityCheck(username, password)

    # if (password != password_check):
    #    print("Password does not match. Please try again!")
    #    getInput()
    # else:
    #    validityCheck(username, password, email)


def validityCheck(username, password):
    cur.execute("SELECT rowid FROM ACCOUNTS WHERE username = ?", (username,))
    data = cur.fetchone()
    if data is None:
        print('There is no entry for %s' % username)

        #cur.execute("SELECT rowid FROM ACCOUNTS WHERE email = ?", (email,))
        #data = cur.fetchone()
        # if data is None:
        #    print('There is no entry for %s' % email)

        #if re.search('^[a-zA-Z0-9_!#$%&’*+/=?`{|}~^.-]+@[a-zA-Z0-9.-]+$', email):
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
        #else:
        #    print("Invalid Email!")
        #    getInput()
        #    return
        # else:
        #    print('Found email %s in Database at row %s' % (email, data[0]))
    else:
        print('Found username %s in Database at row %s' % (username, data[0]))


def insertUser(username, password):
    cur.execute("INSERT INTO ACCOUNTS (username, password) VALUES (?,?)",
                (username, str(password)))
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
