import sys

def read_edge_file(filepath):
    with open(filepath) as filehandle:
        n_nodes, n_edges = filehandle.readline().rstrip().split()
        degree_array = [0] * int(n_nodes)
        for line in filehandle:
            node1, node2 = line.rstrip().split()
            degree_array[int(node1) - 1] += 1
            degree_array[int(node2) - 1] += 1
    
    answer = ""
    for degree in degree_array:
        answer = f"{answer}{degree} "
    
    return answer
    
if __name__ == "__main__":
    print(read_edge_file(sys.argv[1]))