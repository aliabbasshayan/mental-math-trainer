# Mental Math Trainer

A Python OOP-based console mental math trainer.  Practice addition,
subtraction, and multiplication with progressively harder questions and instant
feedback.

---

## Features

- **10 questions** per session, cycling through +, −, and × operations
- **Progressive difficulty** – numbers grow with each question
  (`num1 = (i+1)*10`, `num2 = (i+1)*5`)
- **Immediate feedback** – correct/wrong shown after every answer; wrong
  answers reveal the correct result
- **Final score summary** – total, correct, incorrect, and percentage
- **Error handling** – invalid (non-integer) inputs are caught gracefully
- **PEP 8 compliant** with full docstrings

---

## Project Structure

```
mental-math-trainer/
├── main.py                 # Entry point
├── math_question.py        # MathQuestion class
├── quiz.py                 # Quiz class
├── mental_math_trainer.py  # MentalMathTrainer class (console)
└── README.md
```

---

## Requirements

- Python 3.8 or newer

No third-party packages are required.

---

## Usage

```bash
python main.py
```

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

---

## License

MIT
