import numpy as np


class Simulation:
    X0 = 0.0
    Y0 = 1.0
    Z0 = 1.0
    NUM_STEPS = int(1.e3)
    STEP = 5 * 1.e-5

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.xs = np.empty(Simulation.NUM_STEPS + 1)
        self.ys = np.empty(Simulation.NUM_STEPS + 1)
        self.zs = np.empty(Simulation.NUM_STEPS + 1)
        self.xs[0] = Simulation.X0
        self.ys[0] = Simulation.Y0
        self.zs[0] = Simulation.Z0

    def simulate_attractor(self):
        x, y, z = Simulation.X0, Simulation.Y0, Simulation.Z0
        t = 0.0
        for i in range(1, Simulation.NUM_STEPS + 1):
            t += Simulation.STEP
            x, y, z = self.RungeKutta4(x, y, z, t)
            self.xs[i] = x
            self.ys[i] = y
            self.zs[i] = z

    # noinspection PyPep8Naming,DuplicatedCode
    def RungeKutta4(self, x, y, z, t):
        k_1 = self.x_formula(x, y)
        l_1 = self.y_formula(x, y, z)
        m_1 = self.z_formula(x, y, z)

        RKx = x + k_1 * t * 0.5
        RKy = y + l_1 * t * 0.5
        RKz = z + m_1 * t * 0.5
        k_2 = self.x_formula(RKx, RKy)
        l_2 = self.y_formula(RKx, RKy, RKz)
        m_2 = self.z_formula(RKx, RKy, RKz)

        RKx = x + k_2 * t * 0.5
        RKy = y + l_2 * t * 0.5
        RKz = z + m_2 * t * 0.5
        k_3 = self.x_formula(RKx, RKy)
        l_3 = self.y_formula(RKx, RKy, RKz)
        m_3 = self.z_formula(RKx, RKy, RKz)

        RKx = x + k_2 * t
        RKy = y + l_2 * t
        RKz = z + m_2 * t
        k_4 = self.x_formula(RKx, RKy)
        l_4 = self.y_formula(RKx, RKy, RKz)
        m_4 = self.z_formula(RKx, RKy, RKz)

        x += (k_1 + 2 * k_2 + 2 * k_3 + k_4) * t / 6
        y += (l_1 + 2 * l_2 + 2 * l_3 + l_4) * t / 6
        z += (m_1 + 2 * m_2 + 2 * m_3 + m_4) * t / 6

        return x, y, z

    def x_formula(self, x, y):
        return self.a * (y - x)

    def y_formula(self, x, y, z):
        return self.c * x - y - z * x

    def z_formula(self, x, y, z):
        return x * y - self.b * z
