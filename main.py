"""Entry point for the Mental Math Trainer application.

Run this script directly to start the console-based quiz::

    python main.py
"""

from mental_math_trainer import MentalMathTrainer


def main() -> None:
    """Launch the console-based quiz."""
    trainer = MentalMathTrainer()
    trainer.run_console()


if __name__ == "__main__":
    main()
