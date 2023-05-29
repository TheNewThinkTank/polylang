"""_summary_
"""

import json

flashcards = [
    {"question": "Bonjour", "answer": "Hello", "difficulty": "easy"},
    {"question": "Chat", "answer": "Cat", "difficulty": "medium"},
    {"question": "Avion", "answer": "Airplane", "difficulty": "hard"}
]

points = 0


def load_points():
    """Load points data from a file.
    """

    global points
    try:
        with open('points.json') as file:
            points = json.load(file)
    except FileNotFoundError:
        points = {}


def save_points():
    """Save points data to a file.
    """

    with open('points.json', 'w') as file:
        json.dump(points, file)


def handle_answer(correct):
    """Award points for correct answer and update flashcard difficulty.

    :param correct: _description_
    :type correct: _type_
    """

    global points

    if correct:
        points += 10  # Award 10 points for correct answer

    # Update flashcard difficulty based on points
    for flashcard in flashcards:
        difficulty = flashcard['difficulty']
        if difficulty == 'easy' and points >= 20:
            flashcard['difficulty'] = 'medium'
        elif difficulty == 'medium' and points >= 40:
            flashcard['difficulty'] = 'hard'

    save_points()


def get_flashcards(difficulty):
    """Get flashcards based on difficulty ranking.

    :param difficulty: _description_
    :type difficulty: _type_
    :return: _description_
    :rtype: _type_
    """

    return [flashcard for flashcard in flashcards if flashcard['difficulty'] == difficulty]


def main():
    load_points()

    # Use the ranking system to display flashcards
    while True:
        print(f"Current Points: {points}")
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
                question = flashcard['question']
                answer = flashcard['answer']
                user_answer = input(f"Q: {question}?\nA: ")
                correct = user_answer.lower() == answer.lower()
                handle_answer(correct)
                print("Correct!" if correct else "Incorrect!")

        else:
            print("Invalid choice. Please try again.")

    save_points()


if __name__ == '__main__':
    main()
