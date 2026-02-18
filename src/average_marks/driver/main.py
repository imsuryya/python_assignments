import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.calculator import calculate_average


def main():
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks
    
    query_name = input()
    
    average = calculate_average(student_marks[query_name])
    print(f"{average:.2f}")


if __name__ == "__main__":
    main()
