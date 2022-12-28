"""
Reverse palindrome 찾기

1. 기준선 설정 (인덱스 기준)
2. 기준선 인덱스, 기준선 인덱스 +1 를 시작으로 left_nt 와 right_nt(nucleotide) 비교
3. palindrome 기준을 만족하지 않을 경우 break
"""
import sys


def read_sequence(filepath):
    sequence = ""
    subseqs = list()
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                continue
            
            subseqs.append(line.rstrip())
        
        sequence = "".join(subseqs)
    
    return sequence


def main():
    palindrome_relations = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    sequence = read_sequence(sys.argv[1])

    palindrome_seqs = list()
    for idx, nt in enumerate(sequence):
        if idx < 1 or idx >= len(sequence) - 2:
            continue
        
        left_idx = idx
        right_idx = idx + 1
        palindrome_seq_start_pos = 1
        palindrome_seq_length = 0
        while left_idx >= 0 and right_idx < len(sequence) and right_idx - left_idx + 1 <= 14:
            left_nt = sequence[left_idx]
            right_nt = sequence[right_idx]

            if palindrome_relations[left_nt] == right_nt:
                palindrome_seq_start_pos = left_idx + 1
                palindrome_seq_length = right_idx - left_idx + 1

                if palindrome_seq_length >= 4:
                    palindrome_seqs.append((palindrome_seq_start_pos, palindrome_seq_length))

                left_idx -= 1
                right_idx += 1
            else:
                break

    for palindrome in sorted(palindrome_seqs, key=lambda x: x[0]):
        sys.stdout.write(f"{palindrome[0]} {palindrome[1]}\n")
        
        
if __name__ == "__main__":
    main()