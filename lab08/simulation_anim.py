import tkinter as tk
from control_panel import ControlPanel
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from settings import Settings
from tk_screen_set import TkScreenSet


class SimulationAnim(TkScreenSet):
    TITLE = 'Simulation'
    WINDOW_WIDTH = 1500
    WINDOW_HEIGHT = 700

    def __init__(self, simulation):
        super().__init__()
        self.simulation = simulation

        self.title(self.TITLE)
        self.place_window()

        # Visualization settings.
        self.control_panel = ControlPanel(master=self, simulation=simulation)
        self.animation_panel = tk.Frame(self)
        self.animation_panel.grid(row=0, column=1)
        figure, axes = plt.subplots(ncols=2, figsize=(14, 7))
        self.graph = axes[1]
        self.graph.set_xlabel('Temperature[K]')
        self.graph.set_ylabel('Energy[meV]')
        self.image_anim = axes[0].imshow(self.simulation.lattice,
                                         interpolation='nearest',
                                         cmap=cm.get_cmap('coolwarm'),
                                         vmin=-1, vmax=1)

        # Set visibility of number axes of the animation
        self.image_anim.axes.get_xaxis().set_visible(False)
        self.image_anim.axes.get_yaxis().set_visible(False)

        self.canvas = FigureCanvasTkAgg(figure, self.animation_panel)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                         expand=True)

        self.simulation.sim_animation = self

        # Quit settings with multi threading.
        self.protocol(Settings.TK_EXIT_BUTTON_CLICK, self.destroy_simulation)

        self.bind("<<REFRESH>>", self.plot)
        self.bind("<<REFRESH_TEMP_SLIDER>>",
                  lambda unused: self.control_panel.slider_temp.set(
                      self.simulation.temp))

    def destroy_simulation(self):
        """ Turn off simulation and close the window.
        """
        self.simulation.d_temp = 0
        self.simulation.stop()
        self.quit()

    def plot(self, unused):
        """ Make a plot of a lattice.
        """
        self.image_anim.set_data(self.simulation.lattice)
        self.graph.plot(self.simulation.temperatures,
                        self.simulation.energies, color='black')
        self.canvas.draw()
