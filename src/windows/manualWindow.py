import tkinter as tk

from projectConfig import *

class manualWindow(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        self.geometry("750x600")
        self.title("Manual")

        self.initElements()

    def initElements(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        tkList = tk.Listbox(self, height=37, selectmode='browse',justify=tk.LEFT)
        tkList.grid(column=0, row=0, sticky=tk.NW)
        tkList.pack()
        
        i = 0
        for x in projectConfig["gamelist"]:
            tkList.insert(i, x)
            i += 1
        
