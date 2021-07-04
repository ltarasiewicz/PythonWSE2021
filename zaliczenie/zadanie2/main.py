import numbers


def main():
    scores = numbers.rate(1, 100)

    for k, v in scores.items():
        print(f'{k}: {v}')


if __name__ == "__main__":
    main()
