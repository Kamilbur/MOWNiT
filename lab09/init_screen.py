import tkinter as tk
from settings import *
from tk_screen_set import TkScreenSet


class InitScreen(TkScreenSet):
    START_BUTTON_TEXT = 'Start'
    WINDOW_TITLE = 'Startup Screen'
    WINDOW_WIDTH = 372
    WINDOW_HEIGHT = 180

    def __init__(self):
        super().__init__()

        self.place_window()

        # Setup start button
        self.start_button = tk.Button(self, text=InitScreen.START_BUTTON_TEXT)
        self.start_button['command'] = self.finish_startup_stage

        # Override default behaviour of closing window to make whole app quit.
        # There will be opened the second window, so without that statement
        # this window closes and the unwanted simulation begins.
        self.protocol(Settings.TK_EXIT_BUTTON_CLICK, quit)

        self.title(InitScreen.WINDOW_TITLE)

        self.start_button.grid(row=0, column=1)
        # Set appropriate layout.
        tk.Label(self, text=" ").grid(row=1, column=1)
        tk.Label(self, text=" ").grid(row=2, column=2)
        tk.Label(self, text="a: ").grid(row=3, column=0)
        tk.Label(self, text="b: ").grid(row=3, column=1)
        tk.Label(self, text="c: ").grid(row=3, column=2)

        # Make entries for parameters.
        self.entry_a = tk.Entry(self)
        self.entry_b = tk.Entry(self)
        self.entry_c = tk.Entry(self)
        self.entry_a.insert(0, Settings.A)
        self.entry_b.insert(0, Settings.B)
        self.entry_c.insert(0, Settings.C)
        self.entry_a.grid(row=4, column=0)
        self.entry_b.grid(row=4, column=1)
        self.entry_c.grid(row=4, column=2)

        # Set error communicates label.
        self.error_label = tk.Label(self, text="")
        self.error_label.grid(row=5, column=0, columnspan=3)

    # noinspection DuplicatedCode
    def finish_startup_stage(self):
        a_txt = self.entry_a.get()
        b_txt = self.entry_b.get()
        c_txt = self.entry_c.get()

        try:
            a_val = float(a_txt)
            b_val = float(b_txt)
            c_val = float(c_txt)
        except ValueError:
            self.error_label['text'] = "Parameters not valid!"
            self.entry_a.delete(0, tk.END)
            self.entry_b.delete(0, tk.END)
            self.entry_c.delete(0, tk.END)
            self.entry_a.insert(0, Settings.A)
            self.entry_b.insert(0, Settings.B)
            self.entry_c.insert(0, Settings.C)
            return

        if (not (Settings.A_LOWER <= a_val <= Settings.A_UPPER)):
            self.error_label['text'] = "Parameters not valid! A must be in" \
                                       " between " + \
                                       str(Settings.A_LOWER) + \
                                       " and " + \
                                       str(Settings.A_UPPER) + \
                                       " inclusive."
            return
        if (not (Settings.B_LOWER <= b_val <= Settings.B_UPPER)):
            self.error_label['text'] = "Parameters not valid! H must be in" \
                                       " between " + \
                                       str(Settings.B_LOWER) + \
                                       " and " + \
                                       str(Settings.B_UPPER) + \
                                       " inclusive."
            return
        if (not (Settings.C_LOWER < c_val < Settings.C_UPPER)):
            self.error_label['text'] = "Parameters not valid! N must be in" \
                                       " between " + \
                                       str(Settings.C_LOWER) + \
                                       " and " + \
                                       str(Settings.C_UPPER) + \
                                       " inclusive."
            return

        Settings.A = a_val
        Settings.B = b_val
        Settings.C = c_val

        self.destroy()
