import sys


def read_input(filepath):
    main_sequence = ""
    sub_sequence = ""
    
    seq_number = 0
    current_sequence = "None"
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                seq_number += 1
                continue
            
            if seq_number == 1 and not main_sequence:
                current_sequence = "Main"
            if seq_number == 2 and not sub_sequence:
                current_sequence = "Sub"
            
            if current_sequence == "Main":
                main_sequence += line.rstrip()
            elif current_sequence == "Sub":
                sub_sequence += line.rstrip()
    
    return main_sequence, sub_sequence


def main():
    main_sequence, sub_sequence = read_input(sys.argv[1])
    subseq_start_idx = 0
    result = list()
    for subseq_nt in sub_sequence:
        for idx, mainseq_nt in enumerate(main_sequence[subseq_start_idx:]):
            if subseq_nt == mainseq_nt:
                result.append(str(idx + subseq_start_idx + 1))
                subseq_start_idx += idx+1
                break
    
    print(" ".join(result))
    return


if __name__ == "__main__":
    main()