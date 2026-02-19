import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.probability_calculator import calculate_probability


def main():
    """
    Main driver function for the Iterables and Iterators problem.
    """
    n = int(input())
    letters = input().split()
    k = int(input())
    
    probability = calculate_probability(letters, k)
    
    print(f"{probability:.3f}")


if __name__ == "__main__":
    main()
