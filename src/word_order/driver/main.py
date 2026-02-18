import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.counter import count_word_occurrences


def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    
    distinct_count, occurrences = count_word_occurrences(words)
    
    print(distinct_count)
    print(' '.join(map(str, occurrences)))


if __name__ == '__main__':
    main()
