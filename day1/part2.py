"""day 1 advent of code"""


STARTING_POINT = 50


def calculation(value, cobination):
    """
    Compute:
      - how many times the dial hits 0 during this rotation
      - the dial's new final position (0 - 99)

    Args:
        value (int): current dial position
        combination (dict): { "rotation": "L" or "R", "value": steps }
    """
    if cobination["rotation"] == "L":
        exeded_l = 0
        if value == 0:
            exeded_l = cobination["value"] // 100
        elif cobination["value"] < value:
            exeded_l = 0
        else:
            exeded_l = (cobination["value"] - value) // 100 + 1
        return [exeded_l, (value - cobination["value"]) % 100]

    else:
        return [(value + cobination["value"]) // 100,
                (value + cobination["value"]) % 100]


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
        exeded, STARTING_POINT = calculation(STARTING_POINT, elem)
        results.append(exeded)

    print(sum(results))
