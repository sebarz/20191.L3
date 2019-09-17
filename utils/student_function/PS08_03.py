import numpy as np
import networkx as nx
class Graph():

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
                
    def assert_valid_node_number(self, n):
        assert n>=0 and n<self.num_nodes, "invalid node number: %d"%n        
    
    def grade(self, node_number):
        self.assert_valid_node_number(node_number)
        return len(self.nodes[node_number]) if not self.is_directed else self.grade_in(node_number) + self.grade_out(node_number)
    
    def grade_out(self, node_number):
        assert self.is_directed, "only directed graphs have in/out grades"
        self.assert_valid_node_number(node_number)
        
        return len(self.nodes[node_number])

    def grade_in(self, node_number):
        assert self.is_directed, "only directed graphs have in/out grades"
        self.assert_valid_node_number(node_number)
        grade_in = 0
        for i in self.nodes.values():
            if node_number in i: grade_in += 1
   
        return grade_in

    def are_adyacent(self, node_number_1, node_number_2):
        self.assert_valid_node_number(node_number_1)
        self.assert_valid_node_number(node_number_2)
        
        return True if node_number_2 in self.nodes[node_number_1] or node_number_1 in self.nodes[node_number_2] else False
        
    def is_valid_trayectory(self, trayectory):
        assert type(trayectory)==list, "trayectory must be a list"
        
        for i in range(len(trayectory)-1):
            if not self.is_directed and not self.are_adyacent(trayectory[i],trayectory[i+1]):
                return False
            elif not trayectory[i+1] in self.nodes[trayectory[i]]:
                return False
            
        return True
    
