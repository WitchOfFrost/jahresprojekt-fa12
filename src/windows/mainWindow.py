import tkinter as tk
from copy import deepcopy

from windows.aboutWindow import aboutWindow
from windows.gameWindow import gameWindow


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.title("Strategie Prototyp")
        self.windows = {"about": {"count":0, "instances": {}}}

        self.initElements()


    def initElements(self):
        tk.Button(self, text="About", command=lambda: self.openAbout()).pack()
        tk.Button(self, text="Game", command=lambda: self.openGame()).pack()
        self.bind('<Control-q>', lambda void: self.killShortcut())

    def killShortcut(self):
        self.destroy()

    def launch(self):
        self.mainloop()

    def openGame(self):
        gameWindow(self)

    def openAbout(self):
        
        self.windows["about"]["instances"][self.windows["about"]["count"]] = aboutWindow(self)
        self.windows["about"]["count"]+1
            
