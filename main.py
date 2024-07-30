import sounds
import random
from winsound import Beep
import time
import chime

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

score = 0
highscore = 0
letter = ""
answer = ""

print("*** Press Ctrl + C or type 'exit' to exit. ***\n")
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
        score += 1
        chime.success()
        time.sleep(1.2)
    elif answer == "EXIT":
        n = int(open("best.txt", "w"))
        if score > n:
            n.write(score)
        n.close()
        print(f"Your score is {score}. The high score is {highscore}.")
        time.sleep(5)
        exit()
    else:
        print(f"Wrong, it was {letter}.\n\n")
        chime.warning()
        time.sleep(1.2)
