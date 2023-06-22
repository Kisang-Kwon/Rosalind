import os
import sys


def main(sequence):
    i = 0
    
    c_count = 0
    g_count = 0
    skewness = dict()
    min_skewness = 1000000
    while i < len(sequence):
        nt = sequence[i]
        
        if nt == "C":
            c_count += 1
        elif nt == "G":
            g_count += 1

        skewness[i+1] = g_count - c_count
        if g_count - c_count < min_skewness:
            min_skewness = g_count - c_count
            
        i += 1

    output = list()
    for i in skewness:
        if skewness[i] == min_skewness:
            output.append(i)
            
    return output

if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        sequences = list()
        for line in fh:
            sequences.append(line.rstrip())
        
    output = main("".join(sequences))
    
    fh_output = open("output.txt", "w")
    for i in output:
        fh_output.write(f"{i} ")
    fh_output.close()