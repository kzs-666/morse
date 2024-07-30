from winsound import Beep
import time
# from playsound import playsound

SHORT = 450
LONG = 875
PAUSE = 0.015
PAUSE_WAV = 0.11 # calc. by length.py
HERZ = 900
LENGTH = 26

CODE = {"A": "SL",
        "B": "LSSS",
        "C": "LSLS",
        "D": "LSS",
        "E": "S",
        "F": "SSLS",
        "G": "LLS",
        "H": "SSSS",
        "I": "SS",
        "J": "SLLL",
        "K": "LSL",
        "L": "SLSS",
        "M": "LL",
        "N": "LS",
        "O": "LLL",
        "P": "SLLS",
        "Q": "LLSL",
        "R": "SLS",
        "S": "SSS",
        "T": "L",
        "U": "SSL",
        "V": "SSSL",
        "W": "SLL",
        "X": "LSSL",
        "Y": "LSLL",
        "Z": "LLSS"}

""" 
def wavPlay(letter):
    l = CODE[letter]
    for i in range(len(l)):
        if l[i] == "S":
            playsound("short.wav")
        else:
            playsound("long.wav")
        time.sleep(PAUSE_WAV)
 """


def morse(letter):
    l = CODE[letter]
    for i in range(len(l)):
        if l[i] == "S":
            winsound.Beep(HERZ, SHORT)
        else:
            winsound.Beep(HERZ, LONG)
