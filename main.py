import random
import os
import platform
import time


def again():
    print("Do you want to play again?")
    go_or_no = input('Y/N: ')
    if go_or_no == 'Y' or go_or_no == 'y':
        print("Running...")
        time.sleep(2)
        clear()
        go()
    elif go_or_no == 'N' or go_or_no == 'n':
        print("Stopping...")
        time.sleep(2)
        clear()
        return 0


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


print("Welcome to hangman!")
time.sleep(2)
print("You will have ten attempts.")
time.sleep(2)

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def go():
    stop_at = 10
    wrong = 0
    g = load_words()
    a = list(g)
    b = random.choice(a)
    c = len(b)
    d = "-" * c
    print(d)
    word = list(d)
    tries = 0
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
                if '-' in word:
                    break
                else:
                    clear()
                    print("Finished!")
                    time.sleep(2)
                    print(f"The word was, {word}")
                    time.sleep(2)
                    print(f"You got it in {tries} tries with {wrong} mistakes.")
                    time.sleep(2)
                    again()
                tries += 1
            else:
                word = ''.join(word_so_far)
                if wrong == stop_at:
                    print("All over.")
                    clear()
                else:
                    wrong = wrong + 1
                print("Wrong!")
                print(f"{word}")
                print(f"Wrong: {wrong}")
                tries += 1
go()