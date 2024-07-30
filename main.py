import sounds
import random
import winsound
import time

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = ""
answer = ""

print("*** Press Ctrl + C to exit. ***\n")
winsound.Beep(900, 900)
time.sleep(3)
print("Start\n\n")

while (True):
    letter = ALPHABET[random.randint(0, (len(ALPHABET) - 1))]
    sounds.morse(letter)
    answer = input("Letter: ").strip().upper()
    if answer == letter:
        print("Correct!\n\n")
    else:
        print(f"Wrong, it was {letter}.\n\n")