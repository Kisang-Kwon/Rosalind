import sys


def read_input(filepath):
    seq1 = ""
    seq2 = ""
    
    seq_number = 0
    current_sequence = "None"
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                seq_number += 1
                continue
            
            if seq_number == 1:
                seq1 += line.rstrip()
            elif seq_number == 2:
                seq2 += line.rstrip()
    
    return seq1, seq2


def main():
    
    seq1, seq2 = read_input(sys.argv[1])
    transitions = {"A": "G", "T": "C", "G": "A", "C": "T"}
    transversions = {"A": {"T", "C"}, "T": {"A", "G"}, "G": {"C", "T"}, "C": {"G", "A"}}
    
    transition_count = 0
    transversion_count = 0
    for nt1, nt2 in zip(seq1, seq2):
        if transitions[nt1] == nt2:
            transition_count += 1
            
        elif nt2 in transversions[nt1]:
            transversion_count += 1
            
    print(round(transition_count / transversion_count, 11))
    
    
if __name__ == "__main__":
    main()