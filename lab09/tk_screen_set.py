import tkinter as tk


class TkScreenSet(tk.Tk):
    def __init__(self):
        super().__init__()
        self.place_window()

    def place_window(self):
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        window_x = int((screen_width / 2) - (self.WINDOW_WIDTH / 2))
        window_y = int((screen_height / 2) - (self.WINDOW_HEIGHT / 2))
        self.geometry(f"+{window_x}+{window_y}")
