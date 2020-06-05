import tkinter as tk
from control_panel import ControlPanel
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tk_screen_set import TkScreenSet


class SimulationAnim(TkScreenSet):
    TITLE = 'Simulation'
    WINDOW_WIDTH = 850
    WINDOW_HEIGHT = 700

    def __init__(self, simulation):
        super().__init__()
        self.simulation = simulation
        self.simulation.simulate_attractor()

        self.title(self.TITLE)
        self.place_window()

        # Visualization settings.
        self.control_panel = ControlPanel(master=self, simulation=simulation)
        self.animation_panel = tk.Frame(self)
        self.animation_panel.grid(row=0, column=1)
        figure = plt.figure(figsize=(7, 7))
        self.ax = figure.gca(projection='3d')
        self.ax.set_xlabel("X Axis")
        self.ax.set_ylabel("Y Axis")
        self.ax.set_zlabel("Z Axis")
        self.ax.set_title("Lorenz Attractor")

        self.canvas = FigureCanvasTkAgg(figure, self.animation_panel)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                         expand=True)

        self.simulation.sim_animation = self

        self.plot(1)

    def plot(self, unused):
        """ Make a plot of a lattice.
        """

        self.ax.plot(self.simulation.xs, self.simulation.ys,
                     self.simulation.zs)
        self.control_panel.info_label['text'] = 'Wait until rotation is over.'
        for angle in range(0, 180):
            self.ax.view_init(30, angle)
            self.canvas.draw()

        self.control_panel.info_label['text'] = ''
