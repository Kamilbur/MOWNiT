from dataclasses import dataclass
from typing import Any


@dataclass
class Settings:
    # tkinter constants
    TK_EXIT_BUTTON_CLICK: str = 'WM_DELETE_WINDOW'

    N: int = 2 ** 5  # size of the simulation lattice
    J: float = 100
    T: Any = 0.01
    H: float = 0.0
    TEMP = 0.1
    TEMP_LOWER_BOUND = 0.05  # inclusive
    TEMP_STEP: float = 0.01
    TEMP_UPPER_BOUND = 5.0  # inclusive
    N_LOWER_BOUND: int = 1  # exclusive
    N_UPPER_BOUND: int = 257  # exclusive
    J_LOWER_BOUND: int = 1.0  # inclusive
    J_UPPER_BOUND: int = 1000.0  # inclusive
    H_LOWER_BOUND: float = -5.0  # inclusive
    H_STEP: float = 0.01
    H_UPPER_BOUND: float = 5.0  # inclusive

    MC_STEPS: int = 100

    time_delay: float = 0.1
