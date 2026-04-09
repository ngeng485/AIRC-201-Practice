# AIRC 201 Practice

This repository contains coding practice assignments and homework for the AIRC 201 course. It is designed to help students strengthen their Python programming skills through a series of hands-on problems ranging from basic syntax to intermediate algorithmic challenges.

## Repository Structure

The repository is organized by homework assignments. Each folder (e.g., `HW1`, `HW2`) contains:
- `problems.py`: The file where you will implement your solutions.
- `tests.py`: Evaluation scripts to verify your code.
- `README.md`: Specific instructions and problem descriptions for that assignment.

## Setup Instructions

### 1. Prerequisites
Ensure you have **Python 3.12** installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Installation

1. Clone or download this repository.

2. Open a terminal (Terminal, Command Prompt, PowerShell, etc.) in the root directory of this project.

3. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run Tests

Some homework assignments come with a dedicated test suite. You can run these tests to check your progress and correctness. Note that some homework assignments do not have tests. Always read through the `README.md` in the homework folder to check.

To run the tests for a specific homework (e.g., `HW1`), execute the following command from the root directory:

```bash
python HW1/tests.py
```

As new assignments are added (e.g., `HW2`), you will follow the same pattern; for example, run this for `HW2`:

```bash
python HW2/tests.py
```

## Workflow

1. Read the `README.md` inside the specific homework folder (e.g., `HW1/README.md`) to understand the problems.
2. Edit the `problems.py` file in that folder to implement your solutions. In some HWs, there may be multiple problem files of the format `problems_*.py`.
3. Run the `tests.py` script frequently to verify your code. In some HWs, there may be multiple test files of the format `tests_*.py`. In some HWs, there may be no tests. Please read the `README.md` inside the homework folder for case specific instructions.
4. Repeat until all tests pass, or until you finish the desired objective!

## Contributing Solutions

The `student_solutions` folder contains examples of student solutions. Solution contributions are welcome from everyone! Please see `student_solutions/README.md` for instructions on how to contribute.
