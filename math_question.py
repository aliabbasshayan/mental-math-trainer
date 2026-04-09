"""Module containing the MathQuestion class for the Mental Math Trainer."""

import random


class MathQuestion:
    """Represents a single arithmetic question with progressive difficulty.

    The question is generated randomly based on its index (0-9).  Operands
    are drawn from ranges that grow with the index to maintain progressive
    difficulty, and the operation is chosen at random from addition,
    subtraction, and multiplication.
    """

    OPERATIONS = ['+', '-', '*']

    def __init__(self, index: int) -> None:
        """Initialise a MathQuestion for the given question index.

        Args:
            index: Zero-based position of the question in the quiz (0–9).
        """
        self.index = index
        self.num1 = random.randint(10 * (index + 1), 10 * (index + 2))
        self.num2 = random.randint(5 * (index + 1), 5 * (index + 2))
        self.operation = random.choice(self.OPERATIONS)
        self.answer = self._calculate_answer()

    def _calculate_answer(self) -> int:
        """Compute the correct answer for this question.

        Returns:
            The integer result of applying *self.operation* to *self.num1*
            and *self.num2*.
        """
        if self.operation == '+':
            return self.num1 + self.num2
        if self.operation == '-':
            return self.num1 - self.num2
        return self.num1 * self.num2

    def get_question_text(self) -> str:
        """Return the question as a human-readable string.

        Returns:
            A string such as ``"What is 10 + 5?"``
        """
        op_symbol = {'*': '×'}.get(self.operation, self.operation)
        return f"What is {self.num1} {op_symbol} {self.num2}?"

    def check_answer(self, user_answer: int) -> bool:
        """Check whether *user_answer* matches the correct answer.

        Args:
            user_answer: The integer answer provided by the user.

        Returns:
            ``True`` if the answer is correct, ``False`` otherwise.
        """
        return user_answer == self.answer
