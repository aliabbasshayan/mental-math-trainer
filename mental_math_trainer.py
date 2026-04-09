"""Module containing the MentalMathTrainer class.

Provides a console-based quiz experience.
"""

from quiz import Quiz


class MentalMathTrainer:
    """Main application class for the Mental Math Trainer.

    Runs an interactive text-based quiz in the terminal.
    """

    # ------------------------------------------------------------------
    # Console mode
    # ------------------------------------------------------------------

    def run_console(self) -> None:
        """Run the quiz in console (text) mode."""
        print("=" * 50)
        print("       Welcome to Mental Math Trainer!")
        print("=" * 50)
        print(f"You will be asked {Quiz.TOTAL_QUESTIONS} questions.")
        print("Try to answer as many as you can correctly!\n")

        quiz = Quiz()
        while quiz.has_next_question():
            question = quiz.get_current_question()
            q_num = quiz.current_index + 1
            print(f"Question {q_num}/{quiz.TOTAL_QUESTIONS}: "
                  f"{question.get_question_text()}")

            user_answer = self._get_int_input("Your answer: ")
            is_correct = quiz.submit_answer(user_answer)

            if is_correct:
                print("✓ Correct!\n")
            else:
                print(f"✗ Wrong! The correct answer was {question.answer}.\n")

        self._print_summary(quiz)

    @staticmethod
    def _get_int_input(prompt: str) -> int:
        """Prompt the user until a valid integer is entered.

        Args:
            prompt: The text shown to the user.

        Returns:
            The integer entered by the user.
        """
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @staticmethod
    def _print_summary(quiz: Quiz) -> None:
        """Print the final score summary to stdout.

        Args:
            quiz: A completed :class:`Quiz` instance.
        """
        summary = quiz.get_score_summary()
        print("=" * 50)
        print("              Quiz Complete!")
        print("=" * 50)
        print(f"Total questions : {summary['total']}")
        print(f"Correct answers : {summary['correct']}")
        print(f"Wrong answers   : {summary['incorrect']}")
        print(f"Score           : {summary['percentage']}%")
        print("=" * 50)

