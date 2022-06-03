import sys


def read_file(filepath):
    sequences = dict()
    seq_name = str()
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                seq_name = line.rstrip().lstrip(">")
                continue

            if seq_name in sequences:
                sequences[seq_name] += line.rstrip()
            else:
                sequences[seq_name] = line.rstrip()

    return sequences


def get_shortest_sequence(sequences):
    shortest_seq_name = str()
    shortest_seq_len = -1
    for seq_name, seq in sequences.items():
        if shortest_seq_len == -1 or len(seq) < shortest_seq_len:
            shortest_seq_name = seq_name
            shortest_seq_len = len(seq)

    return shortest_seq_name


def subset_generator(sequence):
    for subset_length in range(len(sequence), 0, -1):
        start = 0
        end = len(sequence) - (len(sequence) - subset_length)
        while end <= len(sequence):
            yield sequence[start:end]

            start += 1
            end += 1


def find_longest_common_subset(sequences):
    shortest_seq = get_shortest_sequence(sequences)

    longest_common_subsets = list()
    for subsequence in subset_generator(sequences[shortest_seq]):
        if longest_common_subsets:
            if len(subsequence) != len(longest_common_subsets[0]):
                return longest_common_subsets

        if all(
            [
                subsequence in sequence
                for seq_name, sequence in sequences.items()
                if seq_name != shortest_seq
            ]
        ):
            longest_common_subsets.append(subsequence)

    return longest_common_subsets


def main():
    sequences = read_file(sys.argv[1])
    longest_common_subsets = find_longest_common_subset(sequences)
    print("\n".join(longest_common_subsets))


if __name__ == "__main__":
    main()
