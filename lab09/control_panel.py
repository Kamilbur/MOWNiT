import tkinter as tk
from settings import Settings


class ControlPanel(tk.Frame):
    REDRAW_BUTTON = 'Redraw'
    REDRAW_BUTTON_WIDTH = 20

    def __init__(self, master, simulation):
        super().__init__(master)
        self.simulation = simulation
        self.grid(row=0, column=0)

        # Set pause button.
        self.redraw_button = tk.Button(self, text=ControlPanel.REDRAW_BUTTON)
        self.redraw_button['command'] = self.redraw
        self.redraw_button['width'] = self.REDRAW_BUTTON_WIDTH
        self.redraw_button.grid(row=0, column=0)

        # Set entries
        self.entry_a = tk.Entry(self)
        self.entry_b = tk.Entry(self)
        self.entry_c = tk.Entry(self)
        self.entry_a.insert(0, self.simulation.a)
        self.entry_b.insert(0, self.simulation.b)
        self.entry_c.insert(0, self.simulation.c)
        tk.Label(self, text="a").grid(row=1, column=0)
        tk.Label(self, text="b").grid(row=3, column=0)
        tk.Label(self, text="c").grid(row=5, column=0)
        self.entry_a.grid(row=2, column=0)
        self.entry_b.grid(row=4, column=0)
        self.entry_c.grid(row=6, column=0)

        # Set error label
        self.error_label = tk.Label(self, text="")
        self.error_label.grid(row=7, column=0)
        self.info_label = tk.Label(self, text="")
        self.info_label.grid(row=8, column=0)

    # noinspection DuplicatedCode
    def redraw(self):
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
                                       " between " +\
                                       str(Settings.C_LOWER) +\
                                        " and " +\
                                       str(Settings.C_UPPER) +\
                                       " inclusive."
            return

        self.simulation.a = a_val
        self.simulation.b = b_val
        self.simulation.c = c_val

        self.simulation.simulate_attractor()
        self.master.plot(1)
