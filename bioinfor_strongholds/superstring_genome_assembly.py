import os
import sys
import math

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROSALIND_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(ROSALIND_DIR)

from utils.read_files import read_fasta_file


def find_longest_match(seq1: str, seq2: str):
    match_count = 0
    for i in range(len(seq1)//2):
        seq1_subseq = seq1[len(seq1)//2-i:]
        seq2_subseq = seq2[:math.ceil(len(seq1)/2)+i]
        
        if seq1_subseq == seq2_subseq:
            match_count = len(seq1_subseq)
            
    return match_count

def build_edges(sequences):
    graphs = dict()
    for seq1_id, seq1 in sequences.items():
        for seq2_id, seq2 in sequences.items():
            if seq1_id == seq2_id or seq1_id in graphs and seq2_id in graphs[seq1_id]:
                continue
        
            seq1_to_seq2 = find_longest_match(seq1, seq2)
            seq2_to_seq1 = find_longest_match(seq2, seq1)
            
            if seq1_id not in graphs:
                graphs[seq1_id] = dict()
            
            if seq2_id not in graphs:
                graphs[seq2_id] = dict()
            
            graphs[seq1_id][seq2_id] = seq1_to_seq2
            graphs[seq2_id][seq1_id] = seq2_to_seq1

    return graphs


def layout(node, contig):
    stretched = list()
    stretched.append(node)
    
    if node in contig:
        subset = layout(contig[node], contig)
        stretched += subset
        return stretched
    else:
        return stretched


def main():
    sequences = read_fasta_file(sys.argv[1])
    graph = build_edges(sequences)
    
    contigs = dict()
    root = ""
    check_root = set()
    
    for seq_id, sequence in sequences.items():
        best_match_count = 0
        best_match_seq_id = ""
        for seq2_id, overlap in graph[seq_id].items():
            
            if overlap >= best_match_count:
                best_match_seq_id = seq2_id
                best_match_count = overlap
        
        if best_match_count == 0:
            continue
        
        contigs[seq_id] = best_match_seq_id
        check_root.add(best_match_seq_id)
    
    for seq_id in sequences:
        if seq_id not in check_root:
            root = seq_id
    
    ordered_contigs = layout(root, contigs)
    
    assembly = ""
    for i in range(len(ordered_contigs)-1):
        start_node = ordered_contigs[i]
        end_node = ordered_contigs[i+1]
        overlap = graph[start_node][end_node]
        
        if i == 0:
            assembly += sequences[start_node]
        
        assembly += sequences[end_node][overlap:]
    
    print(assembly)
    
    return


if __name__ == "__main__":
    main()