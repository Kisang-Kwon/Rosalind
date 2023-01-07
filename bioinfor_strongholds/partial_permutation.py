import sys


def main():
    max_number = int(sys.argv[1])
    number_of_permute = int(sys.argv[2])
    
    permutation_count = 1
    for i in range(max_number, max_number - number_of_permute, -1):
        permutation_count *= i
    
    
    sys.stdout.write(f"{permutation_count % 1000000}\n")
    return


if __name__ == "__main__":
    main()