"""day 1 advent of code"""


STARTING_POINT = 50


def calculation(value, cobination):
    """_summary_

    Args:
        value (_type_): _description_
        cobination (_type_): _description_
    """
    if cobination["rotation"] == "L":
        return (value - cobination["value"]) % 100
    else:
        return (value + cobination["value"]) % 100


if __name__ == "__main__":
    rotations = []

    with open("input.txt", "r", encoding="utf-8", newline="\n") as file:

        for line in file:
            combination = {}
            combination["rotation"] = line[0]
            combination["value"] = int(line[1:].replace('\n', ' '))
            rotations.append(combination)

    results = []
    for elem in rotations:
        STARTING_POINT = calculation(STARTING_POINT, elem)
        results.append(STARTING_POINT)

    print(results.count(0))
