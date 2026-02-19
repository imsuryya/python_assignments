import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from util.validator import filter_emails


def main():
    """
    Main driver function for the Email Validator problem.
    """
    n = int(input())
    emails = [input() for _ in range(n)]
    
    valid_emails = filter_emails(emails)
    
    print(valid_emails)


if __name__ == "__main__":
    main()
