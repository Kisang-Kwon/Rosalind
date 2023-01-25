"""
문자열에서 motif 를 찾기 위한 효율적인 알고리즘인 KMP 알고리즘에서 사용되는 
failure array (failure function)을 구현하는 문제

문제는 주어진 시퀀스 S 의 i 번째 subsequence 에서 failure array 의 길이를 찾는 것

Example)
    S = CAGCATGGTATCACAGCAGAG
    
    Solution)
    0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
    
    4번째 값이 1, 5번째 값이 2 인 이유는 S[:4] 은 CAGC 인데 prefix 와 suffix 가 
    한 자리 일치하므로 1, S[:5] 은 CAGCA 로 prefix 와 suffix 가 두 자리 일치하므로 2 가 된다.
"""
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROSALIND_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(ROSALIND_DIR)

from utils.read_files import read_fasta_file


def get_failure_array(sequence):
    len_failure_array = 0
    for i in range(len(sequence)-1):
        suffix_start_idx =  - i - 1
        prefix_end_idx = i+1
        
        prefix = sequence[:prefix_end_idx]
        suffix = sequence[suffix_start_idx:]
        
        if prefix != suffix:
            break
        
        if prefix == suffix:
            len_failure_array = i + 1
    
    return str(len_failure_array)


def main():
    sequences = read_fasta_file(sys.argv[1])
    len_failure_arrays = list()
    for seq_id, sequence in sequences.items():
        for idx in range(1, len(sequence)+1):
            len_failure_array = get_failure_array(sequence[:idx])
            len_failure_arrays.append(len_failure_array)
    
    print(" ".join(len_failure_arrays))
    

if __name__ == "__main__":
    main()