print("Loading board")
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

print("Setting pins")

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.SDA,
        board.SCL,
        board.D4,
        board.D5,
        board.D6,
        board.D7,
        board.D8,

        board.D23,
        board.D20,
        board.D22,
        board.D26,
        board.D27,
        board.D28,
        board.D29,
    )
    row_pins = (
        board.D12,
        board.D13,
        board.D14,
        board.D15,
        board.D16,
    )
    diode_orientation = DiodeOrientation.COL2ROW
