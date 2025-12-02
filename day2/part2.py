"""day 2 advent of code 2025"""
import csv


def extract_numbers(item_ranges):
    """_summary_

    Args:
        item_ranges (_type_): _description_

    Returns:
        _type_: _description_
    """
    number_list = []

    for item_range in item_ranges:
        output = item_range.split("-")
        number_list.append(range(int(output[0]), int(output[1])+1))
    return number_list


def splits(count):
    """_summary_

    Args:
        count (_type_): _description_
    """
    print(count)
    # print range(0, (m+1)*n, n)[1:]


def check_valid_number(number):
    """_summary_

    Args:
        number (_type_): _description_
    """
    splits(number)
    number_to_check = str(number)
    print(number_to_check)

    return 0


if __name__ == "__main__":

    extracted_ranges = []

    with open('input.txt', "r", encoding="utf-8",) as csvfile:
        items_extracted = csv.reader(csvfile, delimiter=',')
        for item_elements in items_extracted:
            extracted_ranges = item_elements

    number_range_list = extract_numbers(extracted_ranges)

    for elem in number_range_list[0]:
        print(elem)
