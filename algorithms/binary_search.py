import sys
import math
from typing import Tuple


def parse_input(filepath: str) -> Tuple:
    with open(filepath) as filehandle:
        n = int(filehandle.readline())
        m = int(filehandle.readline())
        sorted_array = list(map(int, filehandle.readline().split()))
        integer_list = list(map(int, filehandle.readline().split()))
        
    return n, m, sorted_array, integer_list


def binary_search(k, start_idx, end_idx, sorted_array):
    median_idx = math.ceil((end_idx-start_idxb)/2)
    if k == sorted_array[median_idx-1]:
        return median_idx
    else:
        if end_idx - start_idx == 1:
            return -1
        elif k > sorted_array[median_idx-1]:
            start_idx = median_idx + 1
            return binary_search(k, start_idx, end_idx, sorted_array)
        else:
            end_idx = median_idx - 1
            return binary_search(k, start_idx, end_idx, sorted_array)


if __name__ == "__main__":
    filepath = sys.argv[1]
    n, m, sorted_array, integer_list = parse_input(filepath)
    for k in integer_list:
        idx = binary_search(k, 1, n, sorted_array)
        print(idx+1)