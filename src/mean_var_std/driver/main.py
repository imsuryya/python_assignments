import sys
from pathlib import Path
import numpy as np

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.statistics import compute_statistics


def main():
    """
    Main driver function for the Mean, Var, and Std problem.
    """
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    
    mean_result, var_result, std_result = compute_statistics(arr)
    
    print(mean_result)
    print(var_result)
    print(std_result)


if __name__ == "__main__":
    main()
