import sys
import math

def main():
    leaf_nodes = int(sys.argv[1])
    log_to_leaf_nodes = math.log2(leaf_nodes / 3)
    lower_bound_int = math.floor(log_to_leaf_nodes)
    
    internal_nodes = 1
    for i in range(1, lower_bound_int + 1):
        internal_nodes += 3 * 2 ** (i-1)
    
    if leaf_nodes - 3 * 2 ** lower_bound_int != 0:
        internal_nodes += (leaf_nodes - 3 * 2 ** lower_bound_int)
    
    print(internal_nodes)

if __name__ == "__main__":
    main()