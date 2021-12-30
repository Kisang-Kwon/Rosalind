import sys

def insertion_sort(array):
    swap_counts = 0
    for idx in range(1, len(array)):
        cursor = idx
        while cursor > 0 and array[cursor-1] > array[cursor]:
            swap_counts+=1
            array[cursor-1], array[cursor] = array[cursor], array[cursor-1]
            cursor = cursor - 1
            
    return array, swap_counts

if __name__ == "__main__":
    with open(sys.argv[1]) as filehandle:
        filehandle.readline()
        for line in filehandle:
            arr = list(map(int, line.rstrip().split()))
            
    sorted_array, swaps = insertion_sort(arr)
    #print(sorted_array, swaps)
    print(swaps)