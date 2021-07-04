def factorial(num: int) -> int:
    if num < 0:
        raise Exception("Factorial for negative numbers is undefined")

    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)
