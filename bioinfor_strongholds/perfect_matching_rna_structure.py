import sys


def read_rna_sequence(filepath):
    rna_seq = {
        "A": 0, "C": 0
    }
    
    with open(filepath) as fh:
        for line in fh:
            if line.startswith(">"):
                continue
            
            for nt in line:
                if nt == "A":
                    rna_seq["A"] += 1
                elif nt == "C":
                    rna_seq["C"] += 1
    
    return rna_seq


def factorial(n):
    result = 1
    for number in range(1, n+1):
        result *= number
    
    return result

def main():
    rna_seq = read_rna_sequence(sys.argv[1])
    
    sys.stdout.write(f"{factorial(rna_seq['A']) * factorial(rna_seq['C'])}" + "\n")
    
    
if __name__ == "__main__":
    main()