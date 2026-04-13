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
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)



    for key in data:
        keys.append(key)

    print(f"Klíče: {keys}")
    if field not in keys:
        return "None"

    for key, value in data.items():
        if key == field:
            return value


    # get current working directory path
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name


def linear_search(search_field, look_num):
    result = {"positions":"","count":""}
    indexs = []
    count = 0

    for index, value in enumerate(search_field):

        if value == look_num:
            indexs.append(index)
            count += 1

    result["positions"] = indexs
    result["count"] = count
    print(indexs)
    print(count)
    return result

def main():
    sequential_data = (read_data("sequential.json", "unordered_numbers"))
    print(sequential_data)
    print(linear_search(sequential_data, 5))

if __name__ == "__main__":
    main()
