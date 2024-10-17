# Copyright 2022 Manna Harbour
# github.com/manna-harbour/miryoku
# generated
# AKSHULLY THO, I generated a file for a different keyboard and modified it into this
# to fit my handwired keeb.

print("Starting KMK")

from kb import KMKKeyboard
from kmk.keys import KC
keyboard = KMKKeyboard()
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.holdtap import HoldTap; keyboard.modules.append(HoldTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())

print("Setting keymap")
keyboard.keymap = [
     # BASE
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

          KC.NO, KC.W, KC.E, KC.R, KC.T, KC.NO, KC.NO, KC.NO, KC.NO, KC.Y, KC.U, KC.I, KC.O, KC.NO,

          KC.Q,
          KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.G,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.H,
          KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.QUOT,

          KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.C,
          KC.V,
          KC.B,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.N,
          KC.M,
          KC.COMM,
          KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.P, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),

          KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.NO,
          KC.NO,
          KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.NO,
          KC.NO,
          KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.NO,
          KC.NO,
          KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),
     ],
     # EXTRA
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

          KC.Q, KC.W, KC.E, KC.R, KC.T, KC.NO, KC.NO, KC.NO, KC.NO, KC.Y, KC.U, KC.I, KC.O, KC.QUOT,

          KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.G,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.H,
          KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.HT(KC.P, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),

          KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.C,
          KC.V,
          KC.B,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.NO,
          KC.N,
          KC.M,
          KC.COMM,
          KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200),
          KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),

          KC.NO,
          KC.NO,
          KC.NO,
          KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.NO,
          KC.NO,
          KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),
          KC.NO,
          KC.NO,
          KC.NO
     ],
     # TAP
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.Q, KC.W, KC.E, KC.R, KC.T, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.Y, KC.U, KC.I, KC.O, KC.P,
          KC.A, KC.S, KC.D, KC.F, KC.G, KC.NO, KC.NO, KC.NO, KC.NO, KC.H, KC.J, KC.K, KC.L, KC.QUOT,
          KC.Z, KC.X, KC.C, KC.V, KC.B, KC.NO, KC.NO, KC.NO, KC.NO, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
          KC.NO, KC.NO, KC.DEL, KC.BSPC, KC.ENT, KC.NO, KC.NO, KC.NO, KC.TAB, KC.SPC, KC.ESC, KC.NO, KC.NO, KC.NO
     ],
     # BUTTON
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTL(KC.Y), KC.LCTL(KC.V), KC.LCTL(KC.C), KC.LCTL(KC.X), KC.LCTL(KC.Z),
          KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
          KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTL(KC.Y), KC.LCTL(KC.V), KC.LCTL(KC.C), KC.LCTL(KC.X), KC.LCTL(KC.Z),
          KC.NO, KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.NO, KC.NO, KC.NO
     ],
     # NAV
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.PGUP, KC.HOME, KC.UP, KC.END, KC.INS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
          KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, KC.TD(KC.CW, KC.CAPS, tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
          KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.RALT, KC.NO,
          KC.NO, KC.NO, KC.NO, KC.DEL, KC.BSPC, KC.ENT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
     ],
     # MOUSE
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.MW_UP, KC.NO, KC.MS_UP, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
          KC.MW_DN, KC.MS_LT, KC.MS_DN, KC.MS_RT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
          KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.RALT, KC.NO,
          KC.NO, KC.NO, KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
     ],
     # MEDIA
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.NO, KC.NO, KC.VOLU, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
          KC.NO, KC.MPRV, KC.VOLD, KC.MNXT, KC.PS_TOG, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
          KC.NO, KC.NO, KC.NO, KC.NO, KC.HID, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.RALT, KC.NO,
          KC.NO, KC.NO, KC.NO, KC.MUTE, KC.MPLY, KC.MSTP, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
     ],
     # NUM
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC,
          KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.EQL, KC.N4, KC.N5, KC.N6, KC.SCLN,
          KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.BSLS, KC.N1, KC.N2, KC.N3, KC.GRV,
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MINS, KC.N0, KC.DOT, KC.NO, KC.NO, KC.NO
     ],
     # SYM
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
          KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR,
          KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PLUS, KC.DLR, KC.PERC, KC.CIRC, KC.COLN,
          KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PIPE, KC.EXLM, KC.AT, KC.HASH, KC.TILD,
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.UNDS, KC.LPRN, KC.RPRN, KC.NO, KC.NO, KC.NO
     ],
     # FUN
     [
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

          KC.TD(KC.NO, KC.RELOAD, tap_time=200),
          KC.TD(KC.NO, KC.DF(2), tap_time=200),
          KC.TD(KC.NO, KC.DF(1), tap_time=200),
          KC.TD(KC.NO, KC.DF(0), tap_time=200),
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PSCR, KC.F7, KC.F8, KC.F9, KC.F12,

          KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.SLCK, KC.F4, KC.F5, KC.F6, KC.F11,

          KC.NO,
          KC.RALT,
          KC.TD(KC.NO, KC.DF(6), tap_time=200),
          KC.TD(KC.NO, KC.DF(9), tap_time=200),
          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PAUS, KC.F1, KC.F2, KC.F3, KC.F10,

          KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TAB, KC.SPC, KC.ESC, KC.NO, KC.NO, KC.NO,
     ],
]

layer_names_list = [
"Base", "Extra", "Tap", "Button", "Nav", "Mouse", "Media", "Num", "Sym", "Fun",
]

if __name__ == '__main__':
     print('Miryoku-ish KMK configured')
     keyboard.go()
