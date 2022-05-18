import tkinter as tk


class gameWindow(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        self.geometry("500x500")
        self.title("Game")
