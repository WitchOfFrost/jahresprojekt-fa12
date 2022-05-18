import tkinter as tk
from projectConfig import *


class aboutWindow(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        self.geometry("300x300")
        self.title("About")

        self.initGuiElements()

    def initGuiElements(self):
        
        ### Text ###

        self.text1 = tk.Text(self, width=250, height=250,
                             padx=25, pady=25, bd=2, cursor="xterm")
        self.text1.tag_config("center", justify='center')

        self.text1.configure(font=("Roboto", 20, "bold"))
        self.text1.insert("1.0", "About\n\n")
        self.text1.insert(tk.END, "Version: " + projectConfig["version"])






        ### Complete ####

        self.text1.tag_add("center", "1.0", "end")
        self.text1.config(state=tk.DISABLED)
        self.text1.pack()
