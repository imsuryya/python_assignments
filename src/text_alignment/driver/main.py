import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.logo_printer import print_rangoli


def main():
    thickness = int(input())
    print_rangoli(thickness)


if __name__ == '__main__':
    main()
