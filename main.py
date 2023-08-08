import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
print("Welcome to hangman!")
print("You will have five attempts")

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


clear()
stop_at = 6
wrong = 0
g = load_words()
a = list(g)
b = random.choice(a)
c = len(b)
d = "-" * c
print(d)
while True:


    def get_single_letter_input():
        while True:
            guess = input("Enter a letter: ")
            if len(guess) == 1:
                return guess


    word_so_far = "".join("-" for letter in b)
    for n in range(5):
        guess = get_single_letter_input()
        if guess in b:
            word_so_far = "".join(x if x in guess else word_so_far[i]
                                  for i, x in enumerate(b))

            print(f"{word_so_far}")
            print(f"Wrong: {wrong}")
        else:
            print("Wrong!")
            if wrong == stop_at:
                print("All over.")
                break
            else:
                wrong = wrong + 1
