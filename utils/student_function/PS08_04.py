import numpy as np
class Graph:
    def __init__(self, num_nodes, edge_list):
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
        
        self.num_nodes  = num_nodes
        self.inc_matrix = m = np.zeros((num_nodes, len(edge_list)), dtype=int)
        
        for i in range(m.shape[1]):
            m[edge_list[i][0],i] = 1
            m[edge_list[i][1],i] = 1
