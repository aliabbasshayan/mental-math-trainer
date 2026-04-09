"""Module containing the MentalMathTrainer class.

Provides both a console-based and a Tkinter GUI-based quiz experience.
"""

try:
    import tkinter as tk
    from tkinter import messagebox
    _TKINTER_AVAILABLE = True
except ImportError:  # pragma: no cover – tkinter is a standard-library module
    _TKINTER_AVAILABLE = False

from quiz import Quiz


class MentalMathTrainer:
    """Main application class for the Mental Math Trainer.

    Supports two modes of operation:
    * **Console mode** – runs an interactive text-based quiz in the terminal.
    * **GUI mode** – opens a Tkinter window with a welcome screen, question
      display, answer input, progress indicator, and results screen.
    """

    FEEDBACK_DELAY_MS = 900  # milliseconds before advancing to the next screen

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

    # ------------------------------------------------------------------
    # GUI mode
    # ------------------------------------------------------------------

    def run_gui(self) -> None:
        """Launch the Tkinter GUI for the quiz."""
        if not _TKINTER_AVAILABLE:
            print("Tkinter is not available in this environment. "
                  "Please install it or use console mode instead.")
            return

        self._root = tk.Tk()
        self._root.title("Mental Math Trainer")
        self._root.geometry("500x400")
        self._root.resizable(False, False)
        self._root.configure(bg="#f0f4f8")

        self._quiz = None
        self._answer_var = tk.StringVar()
        self._feedback_var = tk.StringVar()

        self._show_welcome_screen()
        self._root.mainloop()

    # ---- Screens ----

    def _clear_window(self) -> None:
        """Remove all widgets from the root window."""
        for widget in self._root.winfo_children():
            widget.destroy()

    def _show_welcome_screen(self) -> None:
        """Display the welcome/start screen."""
        self._clear_window()

        tk.Label(
            self._root,
            text="🧮 Mental Math Trainer",
            font=("Helvetica", 22, "bold"),
            bg="#f0f4f8",
            fg="#2d3748",
        ).pack(pady=40)

        tk.Label(
            self._root,
            text=f"Test your mental arithmetic with {Quiz.TOTAL_QUESTIONS} "
                 "progressively harder questions!",
            font=("Helvetica", 12),
            bg="#f0f4f8",
            fg="#4a5568",
            wraplength=400,
            justify="center",
        ).pack(pady=10)

        tk.Button(
            self._root,
            text="Start Quiz",
            font=("Helvetica", 14, "bold"),
            bg="#4299e1",
            fg="white",
            activebackground="#3182ce",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            command=self._start_quiz,
        ).pack(pady=40)

    def _start_quiz(self) -> None:
        """Initialise a new quiz and show the first question."""
        self._quiz = Quiz()
        self._answer_var.set("")
        self._feedback_var.set("")
        self._show_question_screen()

    def _show_question_screen(self) -> None:
        """Render the question screen for the current question."""
        self._clear_window()

        quiz = self._quiz
        question = quiz.get_current_question()
        q_num = quiz.current_index + 1

        # Progress label
        tk.Label(
            self._root,
            text=f"Question {q_num} of {quiz.TOTAL_QUESTIONS}",
            font=("Helvetica", 11),
            bg="#f0f4f8",
            fg="#718096",
        ).pack(pady=(20, 5))

        # Progress bar (canvas)
        progress_canvas = tk.Canvas(
            self._root, width=400, height=16, bg="#e2e8f0",
            highlightthickness=0,
        )
        progress_canvas.pack()
        fill_width = int(400 * q_num / quiz.TOTAL_QUESTIONS)
        progress_canvas.create_rectangle(
            0, 0, fill_width, 16, fill="#4299e1", outline=""
        )

        # Question text
        tk.Label(
            self._root,
            text=question.get_question_text(),
            font=("Helvetica", 20, "bold"),
            bg="#f0f4f8",
            fg="#2d3748",
            wraplength=450,
            justify="center",
        ).pack(pady=30)

        # Answer entry
        self._answer_var.set("")
        answer_entry = tk.Entry(
            self._root,
            textvariable=self._answer_var,
            font=("Helvetica", 16),
            justify="center",
            width=10,
            relief="solid",
        )
        answer_entry.pack()
        answer_entry.focus_set()
        answer_entry.bind("<Return>", lambda _: self._submit_gui_answer())

        # Submit button
        tk.Button(
            self._root,
            text="Submit",
            font=("Helvetica", 13, "bold"),
            bg="#48bb78",
            fg="white",
            activebackground="#38a169",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=8,
            command=self._submit_gui_answer,
        ).pack(pady=15)

        # Feedback label (populated after answer)
        self._feedback_label = tk.Label(
            self._root,
            textvariable=self._feedback_var,
            font=("Helvetica", 12),
            bg="#f0f4f8",
        )
        self._feedback_label.pack(pady=5)

    def _submit_gui_answer(self) -> None:
        """Validate the entry, submit the answer, and show feedback."""
        raw = self._answer_var.get().strip()
        try:
            user_answer = int(raw)
        except ValueError:
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a whole number.",
                parent=self._root,
            )
            return

        question = self._quiz.get_current_question()
        is_correct = self._quiz.submit_answer(user_answer)

        if is_correct:
            self._feedback_var.set("✓ Correct!")
            self._feedback_label.config(fg="#276749")
        else:
            self._feedback_var.set(
                f"✗ Wrong! The correct answer was {question.answer}."
            )
            self._feedback_label.config(fg="#c53030")

        # Pause briefly then move on
        self._root.after(self.FEEDBACK_DELAY_MS, self._advance_gui)

    def _advance_gui(self) -> None:
        """Move to the next question or show the results screen."""
        if self._quiz.has_next_question():
            self._show_question_screen()
        else:
            self._show_results_screen()

    def _show_results_screen(self) -> None:
        """Display the final results screen."""
        self._clear_window()
        summary = self._quiz.get_score_summary()

        tk.Label(
            self._root,
            text="🎉 Quiz Complete!",
            font=("Helvetica", 22, "bold"),
            bg="#f0f4f8",
            fg="#2d3748",
        ).pack(pady=30)

        results_text = (
            f"Total Questions : {summary['total']}\n"
            f"Correct Answers : {summary['correct']}\n"
            f"Wrong Answers   : {summary['incorrect']}\n"
            f"Score           : {summary['percentage']}%"
        )
        tk.Label(
            self._root,
            text=results_text,
            font=("Helvetica", 14),
            bg="#f0f4f8",
            fg="#4a5568",
            justify="left",
        ).pack(pady=10)

        tk.Button(
            self._root,
            text="Play Again",
            font=("Helvetica", 13, "bold"),
            bg="#4299e1",
            fg="white",
            activebackground="#3182ce",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=8,
            command=self._show_welcome_screen,
        ).pack(pady=20)

        tk.Button(
            self._root,
            text="Quit",
            font=("Helvetica", 13),
            bg="#fc8181",
            fg="white",
            activebackground="#e53e3e",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=8,
            command=self._root.destroy,
        ).pack()
