import sys



def permute_sign(max_permute_count: int, current_count: int):
    current_count += 1
    signs = [[1], [-1]]
    
    if current_count == max_permute_count:
        return signs
    
    permuted_sequence = list()
    child_sequences = permute_sign(max_permute_count, current_count)
    for sign in signs:
        for child_sequence in child_sequences:
            permuted_sequence.append(sign + child_sequence[:])
            
    return permuted_sequence


def permute_sequence(elements: set):
    if len(elements) == 1:
        return [list(elements)]
    
    permuted_sequences = list()
    for element in elements:
        child_sequences = permute_sequence(elements - {element})
        for child_sequence in child_sequences:
            permuted_sequences.append([element] + child_sequence[:])
    
    return permuted_sequences


def main():
    max_permute_count = int(sys.argv[1])
    permuted_signs = permute_sign(max_permute_count, 0)
    permuted_sequences = permute_sequence(set([i for i in range(1, max_permute_count+1)]))
    
    results = list()
    for sequence in permuted_sequences:
        for sign in permuted_signs:
            results.append(" ".join([str(seq_element * sign_element) for seq_element, sign_element in zip(sequence, sign)]))

    sys.stdout.write(f"{len(results)}\n")
    sys.stdout.write("\n".join(results) + "\n")
    
if __name__ == "__main__":
    main()