import sys
from pathlib import Path
import numpy as np

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.operations import min_max_operation


def main():
    """
    Main driver function for the Min and Max problem.
    """
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    
    result = min_max_operation(arr)
    
    print(result)


if __name__ == "__main__":
    main()
