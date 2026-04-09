"""Entry point for the Mental Math Trainer application.

Run this script directly to choose between console and GUI modes::

    python main.py
"""

from mental_math_trainer import MentalMathTrainer


def main() -> None:
    """Display a mode-selection menu and launch the chosen interface."""
    print("=" * 50)
    print("       Mental Math Trainer")
    print("=" * 50)
    print("Choose a mode:")
    print("  1. Console mode")
    print("  2. GUI mode (Tkinter)")
    print("  q. Quit")
    print("-" * 50)

    trainer = MentalMathTrainer()

    while True:
        choice = input("Enter your choice (1/2/q): ").strip().lower()
        if choice == '1':
            trainer.run_console()
            break
        if choice == '2':
            trainer.run_gui()
            break
        if choice in ('q', 'quit', 'exit'):
            print("Goodbye!")
            break
        print("Invalid choice. Please enter 1, 2, or q.")


if __name__ == "__main__":
    main()
