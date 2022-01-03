import sys
from collections import defaultdict

def align_sequence(shared_motif, query_sequence):
    scored_matrix = defaultdict(dict)
    max_score = 0
    max_score_indices = ""
    
    for i in range(len(query_sequence)+1):
        for j in range(len(shared_motif)+1):
            if i == 0 or j == 0:
                scored_matrix[i][j] = 0
            else:
                if query_sequence[i-1] == shared_motif[j-1]:
                    scored_matrix[i][j] = scored_matrix[i-1][j-1] + 1
                else:
                    scored_matrix[i][j] = scored_matrix[i-1][j-1]
                    
                if scored_matrix[i][j] > max_score:
                    max_score_indices = i - 1
                    max_score = scored_matrix[i][j]
                elif scored_matrix[i][j] == max_score:
                    max_score_indices = i - 1
                    
    
    k = max_score_indices
    #print(k, max_score)
    return query_sequence[k-max_score:k]
            

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
                shared_motif = align_sequence(shared_motif, sequence)
                
    print(shared_motif)