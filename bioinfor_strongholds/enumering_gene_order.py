"""
Permutation 구현하기

"""
import sys


def permutation(permute_numbers: set):
    permuted_sequences = list()
    for n in sorted(permute_numbers):
        next_permute_numbers = permute_numbers - {n}
        
        if not next_permute_numbers:
            permuted_sequences.append(n)
            continue
        
        returned_seqs = list()
        if next_permute_numbers:
            returned_seqs = permutation(next_permute_numbers)        
        
        for returned_seq in returned_seqs:
            permuted_sequences.append(n + " " + returned_seq)
    
    return permuted_sequences


def main():
    permute_numbers = {str(i) for i in range(1, int(sys.argv[1])+1)}
    permuted_sequences = permutation(permute_numbers)
    
    sys.stdout.write(f"{len(permuted_sequences)}\n")
    for seq in permuted_sequences:
        sys.stdout.write(f"{seq}\n")


if __name__ == "__main__":
    main()