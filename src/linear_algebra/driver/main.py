import sys
from pathlib import Path
import numpy as np

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.matrix_operations import calculate_determinant


def main():
    """
    Main driver function for the Linear Algebra problem.
    """
    n = int(input())
    matrix = np.array([input().split() for _ in range(n)], float)
    
    result = calculate_determinant(matrix)
    
    print(result)


if __name__ == "__main__":
    main()
