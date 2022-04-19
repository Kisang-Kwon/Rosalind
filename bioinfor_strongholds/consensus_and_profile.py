import sys
from collections import defaultdict                                                                         


def read_file(filepath: str) -> dict:
    sequences = dict()
    with open(filepath) as filehandle:
        seq_name = "-"
        for line in filehandle:
            if line.startswith(">"):
                seq_name = line.lstrip(">").rstrip()
                continue
            
            if seq_name not in sequences:
                sequences[seq_name] = ""
                
            sequences[seq_name] += line.rstrip()
    
    return sequences


def count_nt(sequences):
    nt_counts = defaultdict(dict)
    for seq_name, sequence in sequences.items():
        for idx, char in enumerate(sequence, 1):
            if idx not in nt_counts:
                nt_counts[idx] = {
                    "A": 0, 
                    "C": 0,
                    "G": 0,
                    "T": 0
                }
            nt_counts[idx][char] += 1
            
    return nt_counts
            

def get_consensus_sequence(nt_counts: dict):
    print_matrix = {
        "A": "A:",
        "C": "C:",
        "G": "G:",
        "T": "T:",
    }
    consensus_sequence = ""
    for idx, counts in nt_counts.items():
        consensus = "-"
        consensus_count = 0
        for base, count in counts.items():
            if count > consensus_count:
                consensus = base
                consensus_count = count
            
            print_matrix[base] += f" {count}"
            
        consensus_sequence += consensus
    
    print(consensus_sequence)
    
    for base, count_str in print_matrix.items():
        print(count_str)
    

if __name__ == "__main__":
    sequences = read_file(sys.argv[1])
    nt_counts = count_nt(sequences)
    get_consensus_sequence(nt_counts)