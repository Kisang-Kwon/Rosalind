import os
import sys


def main(sequence, k: int, L: int, t: int):
    i = 0
    matched_kmers = set()
    while i + L <= len(sequence):
        kmer_count = dict()
        subseq = sequence[i: i+L]
        j = 0
        while j + k <= len(subseq):
            kmer = subseq[j:j+k]
            if kmer not in kmer_count:
                kmer_count[kmer] = 0
            
            kmer_count[kmer] += 1
            j += 1
        
        for kmer in kmer_count:
            if kmer_count[kmer] == t:
                matched_kmers.add(kmer)
                
        i += 1

    return matched_kmers

if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        sequences = list()
        for line in fh:
            if line[0].isdigit():
                k, L, t = line.rstrip().split()
            else:
                sequences.append(line.rstrip())
        
    matched_kmers = main("".join(sequences), int(k), int(L), int(t))
    
    fh_output = open("output.txt", "w")
    for i in matched_kmers:
        fh_output.write(f"{i} ")
    fh_output.close()