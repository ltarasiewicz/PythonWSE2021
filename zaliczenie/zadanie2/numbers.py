from typing import Dict


def rate(start: int, end: int) -> Dict[int, str]:
    scores: Dict[int, str] = {}

    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            scores[i] = 'BEST'
            continue

        elif i % 3 == 0:
            scores[i] = 'GOOD'
            continue

        elif i % 5 == 0:
            scores[i] = 'BETTER'
            continue

        else:
            scores[i] = ''
            continue

    return scores
