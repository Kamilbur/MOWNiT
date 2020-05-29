import tkinter as tk
from settings import Settings


class ControlPanel(tk.Frame):
    SIMULATION_PAUSE = 'Pause simulation'
    SIMULATION_RESUME = 'Resume simulation'
    SIMULATION_RUN_SLIDER_MOVE = 'Move temp slider'
    SIMULATION_STOP_SLIDER_MOVE = 'Stop temp slider'
    PAUSE_BUTTON_WIDTH = 20

    def __init__(self, master, simulation):
        super().__init__(master)
        self.grid(row=0, column=0)
        self.simulation = simulation

        # Set pause button.
        self.pause_button = tk.Button(self, text=self.SIMULATION_PAUSE)
        self.pause_button['command'] = self.simulation_pause_resume
        self.pause_button['width'] = self.PAUSE_BUTTON_WIDTH
        self.pause_button.grid(row=0, column=0)

        # Set sliders.
        def set_slider_temp(value):
            self.simulation.temp = float(value)

        self.slider_temp = tk.Scale(self, from_=Settings.TEMP_LOWER_BOUND,
                                    to=Settings.TEMP_UPPER_BOUND,
                                    orient=tk.HORIZONTAL,
                                    label="temperature: ",
                                    command=set_slider_temp,
                                    resolution=Settings.TEMP_STEP)

        def change_temp_state():
            if (self.run_temp_button['text'] == self.SIMULATION_RUN_SLIDER_MOVE):
                self.simulation.d_temp = Settings.TEMP_STEP
                self.run_temp_button['text'] = self.SIMULATION_STOP_SLIDER_MOVE
            else:
                self.simulation.d_temp = 0
                self.run_temp_button['text'] = self.SIMULATION_RUN_SLIDER_MOVE

        self.run_temp_button = tk.Button(self,
                                         text=self.SIMULATION_RUN_SLIDER_MOVE,
                                         command=change_temp_state)

        def set_slider_h(value):
            self.simulation.h = float(value)

        self.slider_h = tk.Scale(self, from_=Settings.H_LOWER_BOUND,
                                 to=Settings.H_UPPER_BOUND,
                                 orient=tk.HORIZONTAL, label="H: ",
                                 command=set_slider_h,
                                 resolution=Settings.H_STEP)

        def set_slider_speed(value):
            self.simulation.delay_time = 0.5 / int(value)

        self.slider_speed = tk.Scale(self, from_=1, to=10,
                                     orient=tk.HORIZONTAL, label="speed: ",
                                     command=set_slider_speed)

        self.slider_temp.set(Settings.TEMP)
        self.slider_h.set(Settings.H)
        self.slider_speed.set(5)
        self.slider_temp.grid(row=1, column=0)
        self.run_temp_button.grid(row=2, column=0)
        self.slider_h.grid(row=3, column=0)
        self.slider_speed.grid(row=4, column=0)

    def simulation_pause_resume(self):
        if (self.pause_button['text'] == self.SIMULATION_RESUME):
            self.simulation.unpause()
            self.pause_button['text'] = self.SIMULATION_PAUSE
        else:
            self.simulation.pause()
            self.pause_button['text'] = self.SIMULATION_RESUME
