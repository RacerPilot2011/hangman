import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


print("Welcome to hangman!")
print("You will have ten attempts")


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
stop_at = 6
wrong = 0
g = load_words()
a = list(g)
b = random.choice(a)
c = len(b)
d = "-" * c
print(d)
word = list(d)
gues = ""
while True:

    def get_single_letter_input():
        while True:
            gues = input("Enter a letter: ")
            if len(gues) == 1:
                return gues


    word_so_far = "".join("-" for letter in b)
    for n in range(10):
        guess = get_single_letter_input()
        if guess in b:
            word_so_far = "".join(x if x in guess else word_so_far[i]
                                  for i, x in enumerate(b))

            word_so_far = list(word_so_far)
            wor = word_so_far.index(guess)
            word_so_far[wor] = guess
            word = ''.join(word_so_far)
            print(f"{word}")
            print(f"Wrong: {wrong}")
        else:
            if wrong == stop_at:
                print("All over.")
                break
            else:
                wrong = wrong + 1
            print("Wrong!")
            print(f"{word}")
            print(f"Wrong: {wrong}")

