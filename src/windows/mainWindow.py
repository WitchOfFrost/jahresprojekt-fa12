import tkinter as tk

from windows.aboutWindow import aboutWindow
from windows.manualWindow import manualWindow
from windows.gameWindow import gameWindow


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.title("Strategie Prototyp")
        self.windows = {"about": {"count": 0, "instances": {}}}
        self.iconbitmap(default='src/windows/assets/icon.ico')

        self.initElements()

    def initElements(self):
        tk.Button(self, text="Bauernschach",
                  command=lambda: self.openSelectGame("BS")).pack()
        tk.Button(self, text="Dame",
                  command=lambda: self.openSelectGame("DM")).pack()
        tk.Button(self, text="Tic-Tac-Toe",
                  command=lambda: self.openSelectGame("TTT")).pack()
        tk.Button(self, text="Rules", command=lambda: self.openManual()).pack()
        tk.Button(self, text="About", command=lambda: self.openAbout()).pack()
        self.bind('<Control-q>', lambda void: self.killShortcut())

    def killShortcut(self):
        self.destroy()

    def launch(self):
        self.mainloop()

    def openSelectGame(self, mode):
        gameWindow(self, mode)

    def openManual(self):
        manualWindow(self)

    def openAbout(self):
        aboutWindow(self)
