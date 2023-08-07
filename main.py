import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

clear()

stop_at = 0
wrong = 0
g = load_words()
a = list(g)
b = random.choice(a)
c = len(b)
d = "-" * c
print(d)
while True:
    e = input("Letter:")
    if e in b:
        clear()
        print("")
    else:
        print("no!")
