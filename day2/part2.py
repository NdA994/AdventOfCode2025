"""day 2 advent of code 2025"""
import csv
import textwrap


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


def check_valid_number(number):
    """_summary_

    Args:
        number (_type_): _description_
    """
    number_to_check = str(number)
    for i in range(1, (len(number_to_check)//2)+1):
        splits = textwrap.wrap(number_to_check, i)
        print(splits)
        if splits[:-1] == splits[1:]:
            return number
    return 0


if __name__ == "__main__":

    extracted_ranges = []

    with open('input.txt', "r", encoding="utf-8",) as csvfile:
        items_extracted = csv.reader(csvfile, delimiter=',')
        for item_elements in items_extracted:
            extracted_ranges = item_elements

    number_range_list = extract_numbers(extracted_ranges)

    SUM_INVALID_ID = 0
    for id_range in number_range_list:
        for id_number in id_range:
            invalid_id = check_valid_number(id_number)
            SUM_INVALID_ID += invalid_id

    print(SUM_INVALID_ID)
