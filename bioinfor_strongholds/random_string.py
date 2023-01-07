import sys
import math


def read_file(filepath):
    random_sequence = ""
    gc_contents = list()
    
    with open(filepath) as fh:
        random_sequence = fh.readline().rstrip()
        gc_contents = [float(gc_content) for gc_content in fh.readline().rstrip().split()]
    
    return random_sequence, gc_contents


def count_nucleotides(random_sequence):
    nt_counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for nt in random_sequence:
        if nt == "A":
            nt_counts["A"] += 1
        elif nt == "T":
            nt_counts["T"] += 1
        elif nt == "G":
            nt_counts["G"] += 1
        elif nt == "C":
            nt_counts["C"] += 1

    return nt_counts


def main():
    random_sequence, gc_contents = read_file(sys.argv[1])
    nt_counts = count_nucleotides(random_sequence)
    
    result = list()
    for gc_content in gc_contents:
        at_content = 1 - gc_content
        gc_probs = gc_content / 2
        at_probs = at_content / 2
        
        random_seq_probs = (gc_probs ** (nt_counts["G"] + nt_counts["C"])) * (at_probs ** (nt_counts["A"] + nt_counts["T"]))
        result.append(f"{math.log10(random_seq_probs):.3f}")
        
    print(" ".join(result))
    return


if __name__ == "__main__":
    main()