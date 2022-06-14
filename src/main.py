import os
import database.dbCreation as dbCreation
import gui.interface as guiInterface

os.chdir("./src")

dbCreation.createDB(False)
guiInterface.GuiMain()
