
import random

def play_game():

    words = ["python", "apple", "computer", "mobile", "college"]

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6

    print("\n================================")
    print("       WELCOME TO HANGMAN")
    print("================================")
    print("Guess the hidden word!")
    print("You have 6 chances to win.")

    while wrong_guesses < max_guesses:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Wrong guesses:", wrong_guesses)
        print("Remaining chances:", max_guesses - wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won!")
            break

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1

    else:
        print("\nGame Over!")
        print("The correct word was:", word)

    print("\nThanks for playing Hangman!")


while True:

    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if choice != "yes":
        print("\nGoodbye! See you again.")
        break
