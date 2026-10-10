CLI Quiz Application

A command-line quiz application built using Python and JSON. The application loads questions, accepts user answers, calculates scores, and displays a final result summary.

Features

- Loads quiz questions from a separate JSON file.
- Includes 12 multiple-choice questions.
- Randomizes the order of questions.
- Accepts answers using A, B, C, or D.
- Validates user input and handles invalid answers.
- Calculates correct and incorrect answers.
- Displays the final score and percentage.
- Provides explanations for incorrect answers.
- Allows users to quit the quiz early.

Technologies Used

- Python — application logic.
- JSON — storing quiz questions and answers.

Requirements

- Python 3.8 or newer.
- No third-party libraries required.

Project Structure

cli_quiz_application/
├── quiz_app.py
├── questions.json
└── README.md

How to Run the Application

1. Download or clone the project.
2. Ensure that "quiz_app.py" and "questions.json" are in the same folder.
3. Open a terminal in the project folder.
4. Run the following command:

python quiz_app.py

If necessary, use:

python3 quiz_app.py

How to Play

1. Start the application.
2. Read each question and its options.
3. Enter A, B, C, or D to select your answer.
4. Review the feedback provided after each answer.
5. View your final score when the quiz ends.

Enter "Q" to quit the quiz early.

Adding Questions

Open "questions.json" and add questions using the following format:

{
  "question": "What is 2 + 2?",
  "options": [
    "A. 3",
    "B. 4",
    "C. 5",
    "D. 6"
  ],
  "answer": "B",
  "explanation": "Two plus two equals four."
}

Each question should contain a question, a list of options, and the correct answer. The explanation field is optional.

Learning Objectives

This project demonstrates practical use of:

- Python dictionaries and lists.
- Loops and conditional statements.
- Functions and modular programming.
- JSON file handling.
- Input validation and exception handling.
- Random question selection.
- Score calculation and application flow.

Testing

Before submitting the project, test that:

- The quiz starts successfully.
- Questions load correctly.
- Correct and incorrect answers are handled properly.
- Invalid inputs are rejected.
- Scores and percentages are calculated correctly.
- The final summary displays properly.

Internship Submission

For the Veda Technology internship, upload the project to a public GitHub repository. Include the Python source code, JSON question file, and this README.

Submit the repository link through the internship portal and share the completed project on LinkedIn, as required by the task instructions.

Author

Innocent Joseph Matabaro

Python Programming Internship — Task 24

Project: Build a CLI Quiz Application
