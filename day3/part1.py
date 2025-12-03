"""Advent Code Day 3 part 1"""


def charge_calculation(battery_pack_input):
    """_summary_

    Args:
        battery_pack_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_battery = max(battery_pack_input)
    max_index = battery_pack_input.index(max_battery)

    if max_index == (len(battery_pack_input)-1):
        battery_pack_input.pop(max_index)
        first_digit = max(battery_pack_input)
        second_digit = max_battery
    else:
        remain_battery_pack = battery_pack_input[max_index+1:]
        first_digit = max_battery
        second_digit = max(remain_battery_pack)

    concatenate_max = str(first_digit) + str(second_digit)
    return int(concatenate_max)


if __name__ == "__main__":
    battery_stack = []
    with open("input.txt", "r", encoding="utf-8", newline="\n") as file:
        for line in file:
            battery_stack.append(list(line.replace('\n', '')))

    SUM_CHARGE = 0
    for battery_pack in battery_stack:
        charge = charge_calculation(list(map(int, battery_pack)))
        SUM_CHARGE += charge

    print(SUM_CHARGE)
