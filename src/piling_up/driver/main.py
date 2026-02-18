import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.pile_checker import can_pile_up


def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        
        if can_pile_up(cubes):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
