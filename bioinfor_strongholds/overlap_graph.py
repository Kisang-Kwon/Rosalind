import sys


def read_file(filepath):
    seq_name = "-"
    sequences = dict()
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                seq_name = line.rstrip().lstrip(">")
                continue
            
            if seq_name in sequences:
                sequences[seq_name] += line.rstrip()
            else:
                sequences[seq_name] = line.rstrip()
    
    return sequences


def connect_edges(sequences, k):
    edges = []
    for seq1_name, seq1 in sequences.items():
        for seq2_name, seq2 in sequences.items():
            if seq1_name == seq2_name:
                continue
            
            if seq1[-k:] == seq2[:k]:
                edges.append(f"{seq1_name} {seq2_name}")
    
    return edges


if __name__ == "__main__":
    filepath = sys.argv[1]
    k = int(sys.argv[2])
    
    sequences = read_file(filepath)
    edges = connect_edges(sequences, k)
    
    for edge in edges:
        print(edge)