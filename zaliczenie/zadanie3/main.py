import prime


def main():
    results = prime.analyze('source.txt', prime.is_prime)
    for k, v in results.items():
        print(f'{k}: {v}')


if __name__ == "__main__":
    main()
