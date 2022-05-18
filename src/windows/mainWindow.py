import tkinter as tk


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.title("Strategie Prototyp")

    def launch(self):
        self.mainloop()
