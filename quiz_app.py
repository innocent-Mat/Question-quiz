#!/usr/bin/env python3
"""A simple command-line quiz application using questions.json."""

import json
import random
from pathlib import Path

QUESTIONS_FILE = Path(__file__).with_name("questions.json")


def load_questions(path=QUESTIONS_FILE):
    """Load and validate quiz questions from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            questions = json.load(file)
    except FileNotFoundError:
        raise SystemExit(f"Error: Questions file not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Error: Invalid JSON in {path}: {error}")

    if not isinstance(questions, list) or not questions:
        raise SystemExit("Error: questions.json must contain a non-empty list.")

    for number, item in enumerate(questions, start=1):
        required = {"question", "options", "answer"}
        if not isinstance(item, dict) or not required.issubset(item):
            raise SystemExit(f"Error: Question {number} is missing required fields.")
        if not isinstance(item["options"], list) or not item["options"]:
            raise SystemExit(f"Error: Question {number} must have a non-empty options list.")
        if item["answer"].strip().upper() not in {"A", "B", "C", "D"}:
            raise SystemExit(f"Error: Question {number} answer must be A, B, C, or D.")

    return questions


def ask_question(question, number, total):
    """Display one question and return True if answered correctly."""
    print(f"\nQuestion {number} of {total}")
    print(question["question"])
    for option in question["options"]:
        print(f"  {option}")

    valid_answers = {"A", "B", "C", "D"}
    while True:
        answer = input("Your answer (A/B/C/D, or Q to quit): ").strip().upper()
        if answer == "Q":
            return None
        if answer in valid_answers:
            break
        print("Invalid input. Please enter A, B, C, D, or Q.")

    correct = question["answer"].strip().upper()
    if answer == correct:
        print("Correct!")
        return True

    print(f"Incorrect. The correct answer is {correct}.")
    if question.get("explanation"):
        print(f"Explanation: {question['explanation']}")
    return False


def main():
    questions = load_questions()
    random.shuffle(questions)

    print("=" * 42)
    print("          PYTHON CLI QUIZ")
    print("=" * 42)
    print(f"There are {len(questions)} questions.")
    print("Answer using A, B, C, or D. Enter Q to finish early.")

    score = 0
    answered = 0

    for number, question in enumerate(questions, start=1):
        result = ask_question(question, number, len(questions))
        if result is None:
            print("\nQuiz stopped by user.")
            break
        answered += 1
        if result:
            score += 1

    percentage = (score / answered * 100) if answered else 0
    print("\n" + "=" * 42)
    print("             FINAL RESULTS")
    print("=" * 42)
    print(f"Questions answered: {answered}/{len(questions)}")
    print(f"Correct answers:   {score}")
    print(f"Incorrect answers: {answered - score}")
    print(f"Final score:       {percentage:.1f}%")

    if percentage >= 80:
        message = "Excellent work!"
    elif percentage >= 50:
        message = "Good effort—keep practicing."
    else:
        message = "Keep studying and try again."
    print(message)


if __name__ == "__main__":
    main()
