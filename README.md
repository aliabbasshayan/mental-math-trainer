# Mental Math Trainer

A Python OOP-based mental math trainer with both a console interface and a
Tkinter GUI.  Practice addition, subtraction, and multiplication with
progressively harder questions and instant feedback.

---

## Features

- **10 questions** per session, cycling through +, −, and × operations
- **Progressive difficulty** – numbers grow with each question
  (`num1 = (i+1)*10`, `num2 = (i+1)*5`)
- **Immediate feedback** – correct/wrong shown after every answer; wrong
  answers reveal the correct result
- **Final score summary** – total, correct, incorrect, and percentage
- **Dual interface** – console fallback and a Tkinter GUI with a welcome
  screen, progress bar, and results screen
- **Error handling** – invalid (non-integer) inputs are caught gracefully
- **PEP 8 compliant** with full docstrings

---

## Project Structure

```
mental-math-trainer/
├── main.py                 # Entry point – mode-selection menu
├── math_question.py        # MathQuestion class
├── quiz.py                 # Quiz class
├── mental_math_trainer.py  # MentalMathTrainer class (console + GUI)
└── README.md
```

---

## Requirements

- Python 3.8 or newer
- `tkinter` (bundled with the standard CPython distribution)

No third-party packages are required.

---

## Usage

```bash
python main.py
```

You will be presented with a menu:

```
==================================================
       Mental Math Trainer
==================================================
Choose a mode:
  1. Console mode
  2. GUI mode (Tkinter)
  q. Quit
--------------------------------------------------
Enter your choice (1/2/q):
```

### Console mode

Answers are entered at the terminal prompt.  Feedback is printed immediately
and a summary is shown at the end.

```
Question 1/10: What is 10 + 5?
Your answer: 15
✓ Correct!

Question 2/10: What is 20 - 10?
Your answer: 8
✗ Wrong! The correct answer was 10.
...
==================================================
              Quiz Complete!
==================================================
Total questions : 10
Correct answers : 8
Wrong answers   : 2
Score           : 80.0%
==================================================
```

### GUI mode

A Tkinter window opens with:

1. **Welcome screen** – brief description and *Start Quiz* button
2. **Question screen** – progress bar, question text, answer entry, *Submit*
   button, and inline feedback
3. **Results screen** – full score summary with *Play Again* and *Quit*
   buttons

---

## Classes

### `MathQuestion` (`math_question.py`)

| Attribute / Method       | Description                                      |
|--------------------------|--------------------------------------------------|
| `index`                  | Zero-based question number (0–9)                 |
| `num1`, `num2`           | Operands (`(i+1)*10` and `(i+1)*5`)              |
| `operation`              | `'+'`, `'-'`, or `'*'`                           |
| `answer`                 | Pre-computed correct integer answer              |
| `get_question_text()`    | Returns human-readable question string           |
| `check_answer(int)`      | Returns `True` if the given answer is correct    |

### `Quiz` (`quiz.py`)

| Attribute / Method           | Description                                  |
|------------------------------|----------------------------------------------|
| `TOTAL_QUESTIONS`            | Class constant – always 10                   |
| `questions`                  | List of `MathQuestion` instances             |
| `current_index`              | Index of the next unanswered question        |
| `correct_count`              | Running tally of correct answers             |
| `incorrect_count`            | Running tally of wrong answers               |
| `has_next_question()`        | `True` while questions remain                |
| `get_current_question()`     | Returns the current `MathQuestion`           |
| `submit_answer(int)`         | Records answer, advances index, returns bool |
| `get_score_summary()`        | Dict: `total`, `correct`, `incorrect`, `%`   |

### `MentalMathTrainer` (`mental_math_trainer.py`)

| Method          | Description                              |
|-----------------|------------------------------------------|
| `run_console()` | Interactive terminal-based quiz          |
| `run_gui()`     | Tkinter window-based quiz                |

---

## License

MIT
