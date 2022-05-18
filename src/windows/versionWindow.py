import tkinter as tk


class versionWindow(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        self.geometry("100x100")
        self.title("Version")
