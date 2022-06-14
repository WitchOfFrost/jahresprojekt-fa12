import database.dbCreation as dbCreation
import database.userAccountCheck as userAccountCheck
import database.userAccountCreation as userAccountCreation
import database.insertLeaderboard as insertLeaderboard
import gui.interface as guiInterface

dbCreation.createDB()

userAccountCreation.validityCheck("unhappiday", "123456")
userAccountCreation.validityCheck("happiday", "123456")

# insertLeaderboard.insertLeaderboard("unhappiday", 1, 3)
# insertLeaderboard.insertLeaderboard("unhappiday", 1, 1)
# insertLeaderboard.insertLeaderboard("happiday", 1, 3)
# insertLeaderboard.insertLeaderboard("happiday", 1, 2)

guiInterface.GuiMain()
