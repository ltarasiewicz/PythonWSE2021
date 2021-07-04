import age


def main():
    dob: str = input("Provide the year you were born in:\n")
    validator = age.Validator()

    print(validator.message(dob))


if __name__ == "__main__":
    main()
