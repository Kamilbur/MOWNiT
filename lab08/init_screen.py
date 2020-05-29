import tkinter as tk
from settings import *
from tk_screen_set import TkScreenSet


class InitScreen(TkScreenSet):
    SIMULATION_START = 'Start simulation'
    TITLE = 'Startup Screen'
    WINDOW_WIDTH = 372
    WINDOW_HEIGHT = 180

    def __init__(self):
        super().__init__()

        self.place_window()

        # Setup start button
        self.start_button = tk.Button(self, text=self.SIMULATION_START)
        self.start_button['command'] = self.finish_startup_stage

        # Override default behaviour of closing window to make whole app quit.
        # There will be opened the second window, so without that statement
        # this window closes and the unwanted simulation begins.
        self.protocol(Settings.TK_EXIT_BUTTON_CLICK, quit)

        self.title(self.TITLE)

        self.start_button.grid(row=0, column=1)
        # Set appropriate layout.
        tk.Label(self, text=" ").grid(row=1, column=1)
        tk.Label(self, text=" ").grid(row=2, column=2)
        tk.Label(self, text="J: ").grid(row=3, column=0)
        tk.Label(self, text="H: ").grid(row=3, column=1)
        tk.Label(self, text="N: ").grid(row=3, column=2)

        # Make entries for parameters.
        self.entry_j = tk.Entry(self)
        self.entry_h = tk.Entry(self)
        self.entry_n = tk.Entry(self)
        self.entry_j.insert(0, Settings.J)
        self.entry_h.insert(0, Settings.H)
        self.entry_n.insert(0, Settings.N)
        self.entry_j.grid(row=4, column=0)
        self.entry_h.grid(row=4, column=1)
        self.entry_n.grid(row=4, column=2)

        # Set error communicates label.
        self.error_label = tk.Label(self, text="")
        self.error_label.grid(row=5, column=0, columnspan=3)

    def finish_startup_stage(self):
        j_txt = self.entry_j.get()
        h_txt = self.entry_h.get()
        n_txt = self.entry_n.get()

        try:
            j_val = float(j_txt)
            h_val = float(h_txt)
            n_val = int(n_txt)
        except ValueError:
            self.error_label['text'] = "Parameters not valid!"
            self.entry_j.delete(0, tk.END)
            self.entry_h.delete(0, tk.END)
            self.entry_n.delete(0, tk.END)
            self.entry_j.insert(0, Settings.J)
            self.entry_h.insert(0, Settings.H)
            self.entry_n.insert(0, Settings.N)
            return

        if (not (Settings.J_LOWER_BOUND <= j_val <= Settings.J_UPPER_BOUND)):
            self.error_label['text'] = "Parameters not valid! J must be in" \
                                       " between " + \
                                       str(Settings.J_LOWER_BOUND) + \
                                       " and " + \
                                       str(Settings.J_UPPER_BOUND) + \
                                       " inclusive."
            return
        if (not (Settings.H_LOWER_BOUND <= h_val <= Settings.H_UPPER_BOUND)):
            self.error_label['text'] = "Parameters not valid! H must be in" \
                                       " between " + \
                                       str(Settings.H_LOWER_BOUND) + \
                                       " and " + \
                                       str(Settings.H_UPPER_BOUND) + \
                                       " inclusive."
            return
        if (not (Settings.N_LOWER_BOUND < n_val < Settings.N_UPPER_BOUND)):
            self.error_label['text'] = "Parameters not valid! N must be in" \
                                       " between " +\
                                       str(Settings.N_LOWER_BOUND) +\
                                        " and " +\
                                       str(Settings.N_UPPER_BOUND) +\
                                       " exclusive."
            return

        Settings.J = j_val
        Settings.H = h_val
        Settings.N = n_val

        self.destroy()
