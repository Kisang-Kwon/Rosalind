import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROSALIND_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(ROSALIND_DIR)

from utils.read_files import read_fasta_file

def permute_acgt(stack):
    stack += 1
    
    if stack == 4:
        return [["A"], ["C"], ["G"], ["T"]]
    
    subseqs = permute_acgt(stack)
    
    sequences = list()
    for nt in ["A", "C", "G", "T"]:
        sequence = [nt]
        for subseq in subseqs:
            sequences.append(sequence + subseq)
        
    return sequences


def main():
    sequences = read_fasta_file(sys.argv[1])
    kmer_lists = permute_acgt(0)
    
    kmer_count = dict()
    kmer_idx_map = dict()
    for idx, kmer_list in enumerate(kmer_lists):
        kmer_idx_map["".join(kmer_list)] = idx
        # kmer_count["".join(kmer_list)] = 0
    
    kmer_count = [0] * len(kmer_idx_map)
    
    for seq_id, sequence in sequences.items():
        for start_idx in range(len(sequence)-3):
            kmer_seq = sequence[start_idx:start_idx+4]
            kmer_count[kmer_idx_map[kmer_seq]] += 1
            
    print(" ".join(map(str, kmer_count)))
        


if __name__ == "__main__":
    main()