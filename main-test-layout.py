print("Starting KMK")

from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.keymap = [
    [
    KC.GRV, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS, KC.EQL,    KC.BSPC,
    KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC, KC.RBRC,   KC.BSLS,
    KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,KC.EXLM, KC.HASH,   KC.DLR,
    KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.PERC,KC.CIRC, KC.AMPR,   KC.ASTR,
    KC.LPRN,KC.RPRN,KC.UNDS,KC.PLUS, KC.AT, KC.TILD,KC.LCBR,KC.RCBR,KC.PIPE,KC.COLN,KC.DQT, KC.LABK, KC.RABK,   KC.QUES,
    ],
]

if __name__ == '__main__':
    keyboard.go()
