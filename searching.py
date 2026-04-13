from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence, dna_sequence

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

    if field not in keys:
        return "None"

    for key, value in data.items():
        if key == field:
            return value

def linear_search(search_field, look_num):
    result = {"positions":[],"count": ""}
    indexs = []
    count = 0

    start = time.perf_counter()
    for index, value in enumerate(search_field):

        if value == look_num:
            indexs.append(index)
            count += 1

    result["positions"] = indexs
    result["count"] = str(count)
    end = time.perf_counter()
    duration = end - start
    print(f"Lineární měření zabralo {duration:.8f} sekund")
    return result, duration

def binary_search(search_field, look_number):
    start = time.perf_counter()

    left_num_in = 0
    right_num_in = len(search_field) - 1

    while left_num_in <= right_num_in:
        midle_num = (right_num_in + left_num_in) // 2
        if search_field[midle_num] == look_number:
            end = time.perf_counter()
            duration = end - start
            print(f"Binární měření zabralo {duration:.8f} sekund")
            return midle_num, duration

        elif search_field[midle_num] < look_number:
            left_num_in = midle_num + 1

        else:
            right_num_in = midle_num - 1

    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")
    return "None", duration



def graph_maker():
    sizes = []
    times = []
    for size in [100, 500, 1000, 5000, 10000]:
        random_unordered = unordered_sequence(size)
        random_ordered = ordered_sequence(size)

        linear_result = linear_search(random_unordered, 5)
        binary_result = binary_search(random_ordered, 64)

        times1 = linear_result[1]
        times2 = binary_result[1]
        time = times1 - times2

        sizes.append(size)
        times.append(time)

    plt.plot(sizes, times)
    plt.plot(sizes, times)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Graf času lineárního a binárního vyhledávání")
    plt.show()


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    ordered_data = read_data("sequential.json", "ordered_numbers")

    print(sequential_data)
    print(linear_search(sequential_data, 5))
    print(binary_search(ordered_data, 64))
if __name__ == "__main__":
    main()
    graph_maker()