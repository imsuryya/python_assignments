import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.happiness_calculator import calculate_happiness


def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    happiness = calculate_happiness(array, set_a, set_b)
    print(happiness)


if __name__ == '__main__':
    main()
