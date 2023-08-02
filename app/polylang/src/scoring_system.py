"""_summary_
"""

import json
from pprint import pprint as pp

flashcards = [
    {"question": "Bonjour", "answer": "Hello", "difficulty": "easy", "points": 0},
    {"question": "Chat", "answer": "Cat", "difficulty": "medium", "points": 0},
    {"question": "Avion", "answer": "Airplane", "difficulty": "hard", "points": 0},
]


def load_data():
    """Load flashcards and points data from files
    """

    global flashcards
    try:
        with open('flashcards.json') as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []


def save_data():
    """Save flashcards and points data to files
    """

    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)


def handle_answer(flashcard, correct):
    """Award points for correct answer and update flashcard difficulty.

    :param flashcard: _description_
    :type flashcard: _type_
    :param correct: _description_
    :type correct: _type_
    """

    if correct:
        # Award points for correct answer
        flashcard['points'] += 10
    else:
        # Deduct points for incorrect answer
        flashcard['points'] = max(0, flashcard['points'] - 5)

    # Update flashcard difficulty based on points
    points = flashcard['points']
    if points >= 30:
        flashcard['difficulty'] = 'easy'
    elif points >= 20:
        flashcard['difficulty'] = 'medium'
    else:
        flashcard['difficulty'] = 'hard'

    save_data()


def get_flashcards(difficulty):
    """Get flashcards based on difficulty ranking.

    :param difficulty: _description_
    :type difficulty: _type_
    :return: _description_
    :rtype: _type_
    """

    res = [
        flashcard
        for flashcard in flashcards
        if flashcard['difficulty'] == difficulty
           ]

    pp(flashcards)
    print(difficulty)
    pp(res)

    for flashcard in flashcards:
        print(flashcard)

    return res


def main():
    """_summary_
    """

    load_data()

    # Use the ranking system to display flashcards
    while True:
        # print(f"Current Points: {points}")
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("0. Quit")

        choice = input("Enter your choice: ")
        if choice == '0':
            break

        difficulty_mapping = {'1': 'easy', '2': 'medium', '3': 'hard'}
        difficulty = difficulty_mapping.get(choice)
        if difficulty:
            flashcards_to_display = get_flashcards(difficulty)
            if not flashcards_to_display:
                print("No flashcards in this difficulty level.")
                continue

            for flashcard in flashcards_to_display:
                print("############ test ##############")
                question = flashcard['question']
                answer = flashcard['answer']
                user_answer = input(f"Q: {question}?\nA: ")
                correct = user_answer.lower() == answer.lower()
                # handle_answer(correct)
                handle_answer(flashcard, correct)
                print("Correct!" if correct else "Incorrect!")

        else:
            print("Invalid choice. Please try again.")

    # save_points()
    save_data()


if __name__ == '__main__':
    main()
