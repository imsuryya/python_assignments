import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.day_finder import get_day_of_week


def main():
    month, day, year = map(int, input().split())
    print(get_day_of_week(month, day, year))


if __name__ == '__main__':
    main()
