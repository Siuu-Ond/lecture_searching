from pathlib import Path
import json

def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    keys = []

    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)



    for key in data:
        keys.append(key)

    print(f"Klíče: {keys}")
    if field not in keys:
        return "None"

    for key, value in data.items():
        if key == field:
            return value

def linear_search(search_field, look_num):
    result = {"positions":[],"count": ""}
    indexs = []
    count = 0

    for index, value in enumerate(search_field):

        if value == look_num:
            indexs.append(index)
            count += 1

    result["positions"] = indexs
    result["count"] = str(count)

    return result

def binary_search(search_field, look_number):



    left_num_in = 0
    right_num_in = len(search_field) - 1

    while left_num_in <= right_num_in:
        midle_num = (right_num_in + left_num_in) // 2
        if search_field[midle_num] == look_number:
            return midle_num

        elif search_field[midle_num] < look_number:
            left_num_in = midle_num + 1

        else:
            right_num_in = midle_num - 1


    return "None"






def main():
    sequential_data = (read_data("sequential.json", "ordered_numbers"))
    print(sequential_data)
    print(linear_search(sequential_data, 5))
    print(binary_search(sequential_data, 64))
if __name__ == "__main__":
    main()
