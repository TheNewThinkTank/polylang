"""_summary_

Installing TKinter: `brew install python-tk@<PYTHON_VERSION>`
e.g. for Python 3.11:
brew install python-tk@3.11
"""

# TODO: add a menu bar
# TODO: change the layout, or use different widgets
# TODO: add feature: saving progress
# TODO: add feature: keeping score
# TODO: add feature: allow the user to add their own flashcards
# TODO: add feature: support for additional languages

import random

import tkinter as tk

from flashcard import flashcards  # type: ignore
# from mock_flashcards import mock_flashcards
# flashcards = mock_flashcards


class FlashcardGUI:
    """_summary_
    """

    def __init__(self, master):
        self.master = master
        master.title("English Flashcards")

        self.definition_label = tk.Label(master, text="Definition")
        self.definition_label.pack()

        self.definition_text = tk.Text(master, width=40, height=10)
        self.definition_text.pack()

        self.guess_label = tk.Label(master, text="Guess")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.check_button = tk.Button(master, text="Check", command=self.check_guess)
        self.check_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.continue_button = tk.Button(master, text="Continue", command=self.new_flashcard)
        self.continue_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.new_flashcard()

    def new_flashcard(self):
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")

        # Select a random flashcard
        self.word, self.definition = random.choice(list(flashcards.items()))

        # Display the flashcard
        self.definition_text.delete(1.0, tk.END)
        self.definition_text.insert(tk.END, self.definition)

    def check_guess(self):
        guess = self.guess_entry.get().lower()

        # Check the user's guess
        if guess == self.word:
            self.result_label.config(text="Correct! Good job!", fg="green")
        else:
            self.result_label.config(text="Sorry, the correct word is " + self.word + ".", fg="red")

root = tk.Tk()
flashcard_gui = FlashcardGUI(root)
root.mainloop()

print("Thank you for using the English Flashcard Program!")
