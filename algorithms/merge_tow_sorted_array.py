import sys


def get_minimum_number(array_indices: dict, arrays: list):
    min_number = 100001
    for array_idx, number_idx in array_indices.items():
        if array_indices[array_idx] >= len(arrays[array_idx]):
            continue
        
        number = int(arrays[array_idx][number_idx])
        if number < min_number:
            min_number = number
            array_indices[array_idx] += 1
    
    return min_number


def merge_arrays(array_indices: dict, arrays: list):
    merged_array = []
    while(True):
        local_min = get_minimum_number(array_indices, arrays)
        
        if local_min == 100001:
            break
        
        merged_array.append(local_min)

    return merged_array

    
if __name__ == "__main__":
    arrays = []
    array_indices = {}
    with open(sys.argv[1]) as fh:
        for idx, line in enumerate(fh, 1):
            if idx % 2 == 0:
                array_indices[len(arrays)] = 0
                arrays.append(line.rstrip().split())
    
    merged_array = merge_arrays(array_indices, arrays)
    print(" ".join(merged_array))
