import os
import sys

def main(sequence, pattern):
    i = 0
    matched_indice = list()
    while i + len(pattern) <= len(sequence):
        if sequence[i:i+len(pattern)] == pattern:
            matched_indice.append(i)
        i += 1

    return matched_indice

if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        pattern = fh.readline().rstrip()
        sequences = list()
        for line in fh:
            sequences.append(line.rstrip())
        
    matched_indice = main("".join(sequences), pattern)
    
    fh_output = open("output.txt", "w")
    for i in matched_indice:
        fh_output.write(f"{i} ")
    fh_output.close()