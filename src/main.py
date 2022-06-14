import os
import database.dbCreation as dbCreation

os.chdir("./src")

dbCreation.createDB(False)