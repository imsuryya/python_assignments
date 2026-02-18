import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.formatter import print_formatted


def main():
    n = int(input())
    print_formatted(n)


if __name__ == '__main__':
    main()
