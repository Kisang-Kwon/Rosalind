import sys

CODON_TABLE = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "TAA": "-",
        "TAG": "-",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGA": "-",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }


def read_dna_string(filepath):
    sequences = list()
    sequence = ""
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                sequence = ""
                continue
            
            sequence += line.rstrip()
            
        if sequence:
            sequences.append(sequence)

    return sequences


def main():
    sequences = read_dna_string(sys.argv[1])
    
    dna_sequence = sequences[0]
    masking_col = set()
    for sequence in sequences[1:]:
        splicing_start_idx = dna_sequence.index(sequence)
        splicing_end_idx = splicing_start_idx + len(sequence) - 1
        
        for idx in range(splicing_start_idx, splicing_end_idx+1):
            masking_col.add(idx)

    codon = ""
    protein_seq = list()
    for idx, nt in enumerate(dna_sequence):
        if idx in masking_col:
            continue
        
        codon += nt
        
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            if amino_acid == "-":
                break
            protein_seq.append(amino_acid)
            codon = ""
    
    sys.stdout.write("".join(protein_seq) + "\n")


if __name__ == "__main__":
    main()