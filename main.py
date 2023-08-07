from nltk.corpus import words
import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


clear()

stop_at = 0
word_list = words.words()
wrong = 0
a = list(word_list)
b = random.choice(a)
c = len(b)
d = "_" * c
print(d)
while True:
    e = input("Letter:")
    if e in b:
        clear()
        print("")
    else:
        print("no!")
