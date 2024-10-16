def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]


def main() -> None:
    loud_list: list[str] = upper_everything(['Mario', 'james', 'Sara'])
    # Getting mypy errors as desired!
    loud_list2: list[str] = upper_everything([1, 2, 3])
    for string in loud_list:
        print(string)
    for string in loud_list2:
        print(string)

if __file__ == "__main__":
    main()