import sys
from collections import defaultdict

def read_file(filepath: str) -> dict:
    sequences = defaultdict(dict)

    with open(filepath) as filehandle:
        seq_name = ""
        for line in filehandle:
            if line.startswith(">"):
                seq_name = line.lstrip(">").rstrip()
                continue
            
            for idx, char in enumerate(line.rstrip(), 1):
                if idx not in sequences:
                    sequences[idx] = {
                        "A": 0, 
                        "C": 0,
                        "G": 0,
                        "T": 0
                    }
                sequences[idx][char] += 1
            
    return sequences
            

def get_consensus_sequence(sequences: dict):
    print_matrix = {
        "A": "A:",
        "C": "C:",
        "G": "G:",
        "T": "T:",
    }
    consensus_sequence = ""
    for idx, counts in sequences.items():
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
    get_consensus_sequence(sequences)