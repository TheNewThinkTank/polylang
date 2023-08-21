"""Flashcard (also known as an index card) for language learning.
The flash card is bearing information on both sides,
which is intended to be used as an aid in memorization.
Each flashcard bears a question on one side and an answer on the other.
"""

import random

from flashcard import flashcards  # type: ignore
# from mock_flashcards import mock_flashcards
# flashcards = mock_flashcards

print("Welcome to the English Flashcard Program!")
print("---------------------------------------")

while True:
    # Select a random flashcard
    word, definition = random.choice(list(flashcards.items()))

    # Display the flashcard
    print("Definition: " + definition)
    guess = input("What is the word? ")

    # Check the user's guess
    if guess.lower() == word:
        print("Correct! Good job!")
    else:
        print(f"Sorry, the correct word is {word}.")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n) ")
    if choice.lower() != "y":
        break

print("Thank you for using the English Flashcard Program!")
