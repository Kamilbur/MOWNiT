from time import sleep

import numpy as np

from settings import Settings
from stoppable_thread import StoppableThread


class Simulation(StoppableThread):
    MEASUREMENT_PERIOD = 10

    def __init__(self, j, h, n, temp):
        super().__init__()
        self.temp = temp
        self.energies = []
        self.temperatures = []
        self.d_temp = 0
        self.j = j
        self.h = h
        self.n = n
        self.delay_time = Settings.time_delay
        self.lattice = np.full((n, n), 1)
        self.sim_animation = None
        self.idx = 0

    def run(self):
        while (True):
            # Make sure thread closes and pauses.
            if (self.exit_thread):
                break
            if (self.pause_thread):
                continue
            if (self.sim_animation is None):
                continue

            # Main part of loop.
            if (self.sim_animation):
                self.mcmove(1.0 / self.temp, self.n**2)
                self.change_temperature()
                if (self.idx % self.MEASUREMENT_PERIOD == 0):
                    self.energies += [self.get_energy()]
                    self.temperatures += [self.temp]
                if (self.d_temp and not self.exit_thread):
                    self.sim_animation.event_generate("<<REFRESH_TEMP_SLIDER>>")
                if (not self.exit_thread):
                    self.sim_animation.event_generate("<<REFRESH>>")
            sleep(self.delay_time)
            self.idx += 1

    def get_energy(self):
        # Sum of neighbours.
        def nbh_sum(x, y):
            return self.lattice[(x + 1) % self.n, y] + \
                   self.lattice[x - 1, y] + \
                   self.lattice[x, (y + 1) % self.n] + \
                   self.lattice[x, y - 1]

        energy = 0
        for i in range(self.n):
            for j in range(self.n):
                energy -= self.lattice[i, j] * (nbh_sum(i, j) + self.h)

        return energy

    def mcmove(self, beta, steps):
        """ Monte Carlo move using Metropolis algorithm
        """
        n = self.n

        for _ in range(steps):
            x = np.random.randint(0, n)
            y = np.random.randint(0, n)
            s = self.lattice[x, y]
            nbh = (self.lattice[(x + 1) % n, y] +
                   self.lattice[x, (y + 1) % n] +
                   self.lattice[(x - 1) % n, y] +
                   self.lattice[x, (y - 1) % n])
            d_energy = 2 * s * (nbh + self.h)
            if (d_energy < 0):
                s *= -1
            elif (np.random.rand() < np.exp(-d_energy * beta)):
                s *= -1

            self.lattice[x, y] = s

    def get_magnetization(self):
        return np.sum(self.lattice)

    def change_temperature(self):
        if (not (Settings.TEMP_LOWER_BOUND <= self.temp + self.d_temp
                 <= Settings.TEMP_UPPER_BOUND)):
            self.d_temp *= -1
        self.temp += self.d_temp
