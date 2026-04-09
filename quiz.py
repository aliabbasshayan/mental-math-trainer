"""Module containing the Quiz class for the Mental Math Trainer."""

from math_question import MathQuestion


class Quiz:
    """Manages the quiz flow, question progression, and score tracking.

    Attributes:
        questions: Ordered list of :class:`MathQuestion` instances.
        current_index: Index of the question currently being asked.
        correct_count: Number of correctly answered questions so far.
        incorrect_count: Number of incorrectly answered questions so far.
    """

    TOTAL_QUESTIONS = 10

    def __init__(self) -> None:
        """Initialise a new Quiz with 10 progressively harder questions."""
        self.questions = [MathQuestion(i) for i in range(self.TOTAL_QUESTIONS)]
        self.current_index = 0
        self.correct_count = 0
        self.incorrect_count = 0

    # ------------------------------------------------------------------
    # Query helpers
    # ------------------------------------------------------------------

    def has_next_question(self) -> bool:
        """Return ``True`` if there are more questions to answer."""
        return self.current_index < self.TOTAL_QUESTIONS

    def get_current_question(self) -> MathQuestion:
        """Return the current :class:`MathQuestion`.

        Returns:
            The question at *current_index*.

        Raises:
            IndexError: If all questions have already been answered.
        """
        if not self.has_next_question():
            raise IndexError("No more questions in this quiz.")
        return self.questions[self.current_index]

    # ------------------------------------------------------------------
    # Answer processing
    # ------------------------------------------------------------------

    def submit_answer(self, user_answer: int) -> bool:
        """Submit an answer for the current question and advance to the next.

        Updates :attr:`correct_count` or :attr:`incorrect_count` and
        increments :attr:`current_index`.

        Args:
            user_answer: The integer answer provided by the user.

        Returns:
            ``True`` if the answer was correct, ``False`` otherwise.

        Raises:
            IndexError: If all questions have already been answered.
        """
        question = self.get_current_question()
        is_correct = question.check_answer(user_answer)
        if is_correct:
            self.correct_count += 1
        else:
            self.incorrect_count += 1
        self.current_index += 1
        return is_correct

    # ------------------------------------------------------------------
    # Score / summary
    # ------------------------------------------------------------------

    def get_score_summary(self) -> dict:
        """Return a dictionary summarising the quiz results.

        Returns:
            A dict with keys ``total``, ``correct``, ``incorrect``, and
            ``percentage``.
        """
        percentage = (
            (self.correct_count / self.TOTAL_QUESTIONS) * 100
            if self.TOTAL_QUESTIONS > 0
            else 0.0
        )
        return {
            'total': self.TOTAL_QUESTIONS,
            'correct': self.correct_count,
            'incorrect': self.incorrect_count,
            'percentage': round(percentage, 1),
        }
