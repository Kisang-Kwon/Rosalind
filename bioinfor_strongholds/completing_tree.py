"""
서브 그래프 그룹끼리 노드를 모으고 각 서브 그래프를 연결하는 엣지의 개수를 구하는 문제로 해석할 수 있다.
"""

import sys

def get_input(filepath):
    n_nodes = 0
    edges = list()
    with open(filepath) as fh:
        n_nodes = int(fh.readline().rstrip())
        for line in fh:
            edges.append(line.rstrip().split())
    
    return n_nodes, edges


def build_graph(n_nodes, edges):
    node_group = {str(node): 0 for node in range(1, n_nodes+1)}
    group_elements = dict()
    group_max_idx = 0
    
    for edge in edges:
        node1, node2 = edge
        node1_group = node_group[node1]
        node2_group = node_group[node2]
        
        if node1_group == 0 and node2_group == 0:
            group_max_idx += 1
            node_group[node1] = group_max_idx
            node_group[node2] = group_max_idx
            group_elements[group_max_idx] = {node1, node2}
        
        elif node1_group != 0 and node2_group == 0:
            node_group[node2] = node1_group
            group_elements[node1_group].add(node2)
        
        elif node1_group == 0 and node2_group != 0:
            node_group[node1] = node2_group
            group_elements[node2_group].add(node1)
        
        elif node1_group != 0 and node2_group != 0:
            group_elements[node1_group].update(group_elements[node2_group])
            for element_node in group_elements[node2_group]:
                node_group[element_node] = node1_group
                
            del group_elements[node2_group]
    
    for node in node_group:
        if node_group[node] == 0:
            group_max_idx += 1
            group_elements[group_max_idx] = {node}
    
    return group_elements
        

def depth_first_search(node, graph):
    searched_nodes = list()
    searched_nodes.append(node)
    
    for child_node in graph[node]:
        child_graph = depth_first_search(child_node, graph)
        searched_nodes.extend(child_graph)
        
    return searched_nodes
    
    
def main():
    n_nodes, edges = get_input(sys.argv[1])
    graph = build_graph(n_nodes, edges)
    
    print(len(graph) - 1)
        
    return

if __name__ == "__main__":
    main()