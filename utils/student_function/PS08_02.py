import numpy as np
import networkx as nx

class Graph:
    def __init__(self, num_nodes, edge_list, is_directed=False):
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
        
        self.is_directed = is_directed
        self.num_nodes   = num_nodes
        self.nodes = d = {i:[] for i in range(num_nodes)}
             
        for i,j in edge_list:
            if not j in d[i]: d[i].append(j)
            if not is_directed:
                if not i in d[j]: d[j].append(i)
            

        for i in d.values(): i.sort()
                
    def as_nx(self):
        g = nx.DiGraph() if self.is_directed else nx.Graph()
        g.add_nodes_from(self.nodes)
        for i in self.nodes.keys():
            for j in self.nodes[i]:
                g.add_edge(i,j)
        
        return g
    
    def draw(self):
        ng = self.as_nx()
        nx.drawing.draw(ng, arrows=self.is_directed, with_labels=True, 
                        node_alpha=.2, node_color="blue", 
                        node_size=900, font_color="white")
