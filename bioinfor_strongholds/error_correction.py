"""
Error correction

Normal reads appear at least twice in dataset (It could be a reverse complementary.)
Each Read with error appear only once in dataset and their hamming distance is 1.
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROSALIND_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(ROSALIND_DIR)

from utils.read_files import read_fasta_file

def make_reverse_complementary_sequence(sequence):
    nt_pair_matching = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    reverse_complementary_seq = list()
    for nt_idx in range(len(sequence)-1, -1, -1):
        reverse_complementary_seq.append(nt_pair_matching[sequence[nt_idx]])
    
    return "".join(reverse_complementary_seq)
    
    
def get_hamming_distance_is_one(sequence, database):
    for db_seq in database:
        distance = 0
        
        for query_nt, db_nt in zip(sequence, db_seq):
            if query_nt != db_nt:
                distance += 1
            
        if distance == 1:
            return db_seq

    return "-"

def main():
    all_reads = read_fasta_file(sys.argv[1])

    read_count = dict()
    read_appear_once = set()
    for read in all_reads.values():
        reverse_complement_read = make_reverse_complementary_sequence(read)
        
        if read not in read_count:
            read_count[read] = 1
            read_count[reverse_complement_read] = 1
            read_appear_once.add(read)
            continue
        elif read_count[read] == 1:
            read_appear_once.discard(read)
            read_appear_once.discard(reverse_complement_read)
        
        read_count[read] += 1
        read_count[reverse_complement_read] += 1
    
    for read in read_appear_once:
        corrected_read = get_hamming_distance_is_one(read, read_count.keys())
        sys.stdout.write(f"{read}->{corrected_read}\n")
        
        
if __name__ == "__main__":
    main()