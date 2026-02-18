import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.string_processor import merge_the_tools


def main():
    string = input()
    k = int(input())
    merge_the_tools(string, k)


if __name__ == '__main__':
    main()
