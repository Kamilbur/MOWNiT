from settings import Settings
import matplotlib
from simulation import Simulation
from init_screen import InitScreen
from simulation_anim import SimulationAnim
matplotlib.use("TkAgg")


def main():
    # Initial GUI.
    init_gui = InitScreen()
    init_gui.mainloop()

    # Simulation.
    sim = Simulation(Settings.J, Settings.H, Settings.N, Settings.TEMP)
    sim_anim = SimulationAnim(sim)
    sim.start()
    sim_anim.mainloop()


if __name__ == '__main__':
    main()
