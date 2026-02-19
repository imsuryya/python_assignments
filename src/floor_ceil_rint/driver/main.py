import sys
from pathlib import Path
import numpy as np

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.operations import apply_operations


def main():
    """
    Main driver function for the Floor, Ceil and Rint problem.
    """
    arr = np.array(input().split(), float)
    
    floor_result, ceil_result, rint_result = apply_operations(arr)
    
    print(floor_result)
    print(ceil_result)
    print(rint_result)


if __name__ == "__main__":
    main()
