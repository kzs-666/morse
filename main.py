import sounds
import random
from winsound import Beep
import time
import chime

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = ""
answer = ""

print("*** Press Ctrl + C to exit. ***\n")
Beep(900, 900)
time.sleep(3)
print("Start\n\n")

chime.theme("mario")

while (True):
    letter = ALPHABET[random.randint(0, (len(ALPHABET) - 1))]
    sounds.morse(letter)
    answer = input("Letter: ").strip().upper()
    if answer == letter:
        print("Correct!\n\n")
        chime.success()
        time.sleep(1.2)
    else:
        print(f"Wrong, it was {letter}.\n\n")
        chime.warning()
        time.sleep(1.2)
