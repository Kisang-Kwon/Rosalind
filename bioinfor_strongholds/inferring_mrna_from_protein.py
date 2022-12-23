"""
A mod B = n 은 A 를 B 로 나눈 나머지가 n 이라는 의미이다.
a mod n = b mod n 인 a 와 b 를 congruent modulo 라고 부른다. 

Question)
    주어진 단백질 시퀀스를 translation 할 수 있는 mRNA 시퀀스의 총 개수를 N 이라고 할 때, N mod 1,000,000 를 구하기.
    * stop codon 도 고려해야함
"""
import sys

def main():
    codon_table = {
        "F": ["UUU", "UUC"],
        "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
        "I": ["AUU", "AUC", "AUA"],
        "M": ["AUG"],
        "V": ["GUU", "GUC", "GUA", "GUG"],
        "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
        "P": ["CCU", "CCC", "CCA", "CCG"],
        "T": ["ACU", "ACC", "ACA", "ACG"],
        "A": ["GCU", "GCC", "GCA", "GCG"],
        "Y": ["UAU", "UAC"],
        "H": ["CAU", "CAC"],
        "Q": ["CAA", "CAG"],
        "N": ["AAU", "AAC"],
        "K": ["AAA", "AAG"],
        "D": ["GAU", "GAC"],
        "E": ["GAA", "GAG"],
        "C": ["UGU", "UGC"],
        "W": ["UGG"],
        "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "G": ["GGU", "GGC", "GGA", "GGG"],
        "Stop": ["UAA", "UAG", "UGA"],
    }

    protein_seq = sys.argv[1]
    total_number_of_mrna = 1
    for aa in protein_seq:
        codons = codon_table.get(aa.upper())
        total_number_of_mrna *= len(codons)
    
    total_number_of_mrna *= len(codon_table["Stop"])
    
    modulo = total_number_of_mrna % 1000000
    print(modulo)
    return


if __name__ == "__main__":
    main()