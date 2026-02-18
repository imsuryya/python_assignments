import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.score_finder import find_runner_up


def main():
    n = int(input())
    scores = list(map(int, input().split()))
    
    runner_up = find_runner_up(scores)
    print(runner_up)


if __name__ == "__main__":
    main()
