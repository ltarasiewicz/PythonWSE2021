import math
from typing import Dict, Callable


def is_prime(num: int) -> bool:
    if num == 1:
        return False

    for test in range(2, math.floor(num / 2) + 1):
        if num % test == 0:
            return False

    return True


def analyze(file_path: str, prime: Callable[[int], bool]) -> Dict[int, str]:
    results: Dict[int, str] = {}
    with open(file_path, "r") as file:
        for line in file:
            results[int(line.rstrip())] = 'PRIME' if prime(int(line)) else 'NOT PRIME'

    return results
