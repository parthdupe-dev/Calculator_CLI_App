# Python CLI Calculator

## Project Overview

The Python CLI Calculator is a simple command-line application that performs basic arithmetic operations. It allows users to perform calculations through an interactive menu and continues running until the user types `EXIT`.

This project demonstrates fundamental Python programming concepts such as loops, conditional statements, exception handling, user input, and functions.

## Features

- **Addition:** Adds two numbers.
- **Subtraction:** Subtracts the second number from the first.
- **Multiplication:** Multiplies two numbers.
- **Division:** Divides the first number by the second.
- **Continuous Execution:** The calculator runs continuously using a `while` loop.
- **Exit Option:** Type `EXIT` to close the application.
- **Input Validation:** Handles invalid numeric input.
- **Error Handling:** Prevents division by zero.
- **Multiple Operation Inputs:** Supports operation numbers, names, and mathematical symbols.

## Technologies Used

- Python 3
- VS Code / Any Python IDE
- Command Line / Terminal

## Project Structure

```text
Python-CLI-Calculator/
│
├── calculator.py
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Python-CLI-Calculator
```

### 3. Run the Application

```bash
python3 calculator.py
```

## Available Operations

| Option | Operation | Symbol |
|---|---|---|
| 1 | Addition | + |
| 2 | Subtraction | - |
| 3 | Multiplication | * |
| 4 | Division | / |
| EXIT | Exit Calculator | - |

Users can select an operation using its number, name, or mathematical symbol.

## Example Execution

```text
========== PYTHON CALCULATOR ==========
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
Type EXIT to close calculator
=======================================

Enter your choice: 1
Enter the first number: 10
Enter the second number: 20

Result: 30.0

Enter your choice: 3
Enter the first number: 5
Enter the second number: 4

Result: 20.0

Enter your choice: EXIT
Calculator closed. Goodbye!
```

## Error Handling

The application handles the following errors:

1. **ValueError:** Handles invalid numeric input.
2. **ZeroDivisionError:** Handles attempts to divide by zero.
3. **Invalid Operation:** Displays an error message when the user selects an unsupported operation.

## Python Concepts Used

- Variables and Data Types
- User Input (`input()`)
- Type Conversion (`float()`)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- Exception Handling (`try`, `except`)
- `break` and `continue`
- Main Function (`main()`)

## Author

**Parth Nilesh Kabade**

## Project Purpose

This project was developed as part of a Python Developer Internship task to practice Python fundamentals and build an interactive command-line calculator.
