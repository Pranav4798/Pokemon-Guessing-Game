# Hangman in Python

import random

from Wordslist import words, hints
#words = ('apple','orange','coconut','banana','pineapple')

# dictionary of key: ()

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   "
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/   "),
               6: (" o ",
                   "/|\\",
                   "/ \\")
}

def display_man(wrong_guesses):
    print('*********')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    ans = random.choice(words)
    answer = ans.lower()
    print("Welcome to Pokemon Guesser!")
    print("Enter 'clue' for a clue to the pokemon! ( You get only 1 clue )")
    hint = ["_"] * len(answer)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    points = 0

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()


        if guess == 'clue':
            if ans in hints:
                print(f"Your clue is that it's a {hints[ans]}")
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guessed!')
            print(guessed_letters)

        guessed_letters.add(guess)

        if guess == 'clue':
            continue
        elif guess in answer:
            print(guessed_letters)
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            #print(guessed_letters)
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You lose! Try again!')
            is_running = False


if __name__ == '__main__':
    main()
