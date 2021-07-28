#!/usr/bin/python3

from typing import Dict, List, Tuple


def pytuples():
    numbers: Tuple[int, float, int] = (1, 0.51, 1)

def implement_annotations():
    positives: List[int]

    users: Dict[str, int] = {
    "Ecuador": 1,
    "Mexico": 34,
    "Colombia": 45,
    }

    print(type(users))

def main():
    implement_annotations()

if __name__ == "__main__":
    main()
