import sys


def permutation(symbols, n_permute):
    updated_n_permute = n_permute - 1
    
    sequences = list()
    for symbol in symbols:
        if updated_n_permute > 0:
            permute_items = permutation(symbols, updated_n_permute)
            for permute_item in permute_items:
                sequences.append(symbol + permute_item)

        else:
            return symbols
        
    return sequences


def main():
    with open(sys.argv[1]) as fh:
        symbols = sorted(fh.readline().rstrip().split())
        n_permute = int(fh.readline().rstrip())
    
    permute_sequences = permutation(symbols, n_permute)
    
    for seq in permute_sequences:
        sys.stdout.write(f"{seq}\n")


if __name__ == "__main__":
    main()