import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import namedtuple


def main():
    """
    4-line challenge solution:
    n = int(input())
    Student = namedtuple('Student', input().split())
    print(f"{sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n:.2f}")
    """
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    
    total = 0
    for _ in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)
    
    print(f"{total / n:.2f}")


if __name__ == '__main__':
    main()
