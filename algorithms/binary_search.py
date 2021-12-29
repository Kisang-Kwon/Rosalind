import os
import sys

from typing import Tuple


def parse_input(filepath: str) -> Tuple:
    with open(filepath) as filehandle:
        n = int(filehandle.readline())
        m = int(filehandle.readline())
        sorted_array = list(map(int, filehandle.readline().split()))
        integer_list = list(map(int, filehandle.readline().split()))

    return n, m, sorted_array, integer_list


def binary_search(k, start_idx, end_idx, sorted_array):
    median_idx = (start_idx + end_idx) // 2

    if k == sorted_array[median_idx - 1]:
        return median_idx
    else:
        if end_idx - start_idx == 1:
            if k == sorted_array[start_idx - 1]:
                return start_idx
            elif k == sorted_array[end_idx - 1]:
                return end_idx
            else:
                return -1
        elif k > sorted_array[median_idx - 1]:
            if end_idx > median_idx + 1:
                start_idx = median_idx + 1
            else:
                start_idx = median_idx
            return binary_search(k, start_idx, end_idx, sorted_array)
        else:
            if start_idx < median_idx - 1:
                end_idx = median_idx - 1
            else:
                end_idx = median_idx
            return binary_search(k, start_idx, end_idx, sorted_array)


if __name__ == "__main__":
    sys.setrecursionlimit(25000)

    filepath = sys.argv[1]
    n, m, sorted_array, integer_list = parse_input(filepath)
    base_path = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(base_path, "outputs", "binary_search.txt")

    with open(output_path, "w") as output:
        for k in integer_list:
            idx = binary_search(k, 1, n, sorted_array)
            output.write(f"{idx} ")
