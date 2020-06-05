from dataclasses import dataclass


@dataclass
class Settings:
    # tkinter constants
    TK_EXIT_BUTTON_CLICK: str = 'WM_DELETE_WINDOW'

    # Model params
    A: float = 10.0
    A_LOWER: float = 0.0
    A_UPPER: float = 1.e25
    B: float = 2.66
    B_LOWER: float = 0.0
    B_UPPER: float = 1.e5
    C: float = 28.0
    C_LOWER: float = 0.0
    C_UPPER: float = 1.e5
