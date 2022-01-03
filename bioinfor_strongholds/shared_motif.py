import sys
from collections import defaultdict



def find_motif(shared_motif, query_sequence):
    
    for length in range(len(shared_motif)+1, 0, -1):
        start = 0
        for end in range(length):
            
        

    
if __name__ == "__main__":
    shared_motif = ""
    sequences = dict()
    with open(sys.argv[1]) as fh:
        for line in fh:
            if line.startswith(">"):
                seq_name = line.rstrip().lstrip(">")
            else:
                if seq_name in sequences:
                    sequences[seq_name] += line.rstrip()
                else:
                    sequences[seq_name] = line.rstrip()
    
    for sequence in sequences.values():
        if shared_motif == "":
            shared_motif = sequence
        else:
            shared_motif = find_motif({shared_motif}, sequence)
            if not shared_motif:
                print("None")
                
    print(shared_motif)