# Python Assignments

A comprehensive collection of Python programming exercises and HackerRank challenge solutions, organized by topic and concept.

## Topics Covered

This repository covers essential Python concepts and programming fundamentals:

- **Operator Precedence**
- **OOP Concepts** (Object-Oriented Programming)
- **Expressions vs Statements**
- **Type Conversion**
- **Strings**
- **Integers and Floats**
- **Lists, Tuples, and Sets**
- **Dictionaries** - Working with Key-Value Pairs
- **Conditionals and Booleans** - If, Else
- **Loops and Iterations** - For/While Loops
- **Functions**
- **Sorting** - Lists, Tuples, and Objects
- **Lambda, Map, Reduce**
- **Import Modules** and Exploring The Standard Library
- **Working with Dates, Times, Timedeltas, and Timezones**

## HackerRank Challenges

### Basic Python
1. [Finding the Percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem)
2. [Find Second Maximum Number in a List](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)

### Strings
3. [Python Mutations](https://www.hackerrank.com/challenges/python-mutations/problem)
4. [Merge the Tools](https://www.hackerrank.com/challenges/merge-the-tools/problem)
5. [Python String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem)
6. [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem)

### Collections & Data Structures
7. [Collections - Named Tuple](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)
8. [No Idea](https://www.hackerrank.com/challenges/no-idea/problem)
9. [Word Order](https://www.hackerrank.com/challenges/word-order/problem)
10. [Piling Up](https://www.hackerrank.com/challenges/piling-up/problem)

### Date & Time
11. [Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem)
12. [Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem)

### Iterators & Functional Programming
13. [Iterables and Iterators](https://www.hackerrank.com/challenges/iterables-and-iterators/problem)
14. [Validate List of Email Addresses with Filter](https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem)

### NumPy
15. [Floor, Ceil and Rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem)
16. [Min and Max](https://www.hackerrank.com/challenges/np-min-and-max/problem)
17. [Linear Algebra](https://www.hackerrank.com/challenges/np-linear-algebra/problem)
18. [Mean, Var, and Std](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem)

## Project Structure

Each solution follows a consistent structure:

```
src/
├── problem_name/
│   ├── driver/
│   │   ├── __init__.py
│   │   └── main.py          # Main entry point
│   ├── util/
│   │   ├── __init__.py
│   │   └── helper.py        # Utility functions
│   ├── __init__.py
│   └── test_input.txt       # Sample test cases
```

## How to Run

### Individual Solutions

Navigate to the problem's driver directory and run:

```bash
# Method 1: Direct execution
python src/problem_name/driver/main.py

# Method 2: With input file
python src/problem_name/driver/main.py < src/problem_name/test_input.txt

# Method 3: Using pipe (Windows PowerShell)
Get-Content src/problem_name/test_input.txt | python src/problem_name/driver/main.py
```

### Example

```bash
# Run the average marks solution
python src/average_marks/driver/main.py < src/average_marks/test_input.txt

# Run the runner-up score solution
python src/runner_up_score/driver/main.py < src/runner_up_score/test_input.txt
```

## Solutions Implemented

- **Average Marks** - Calculate student grade averages
- **Runner-Up Score** - Find second maximum in a list
- More solutions coming soon...

## Requirements

- Python 3.6+
- NumPy (for NumPy challenges)

## Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [HackerRank Python Track](https://www.hackerrank.com/domains/python)
- [Real Python Tutorials](https://realpython.com/)
