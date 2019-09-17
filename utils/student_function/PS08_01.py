import numpy as np
class Graph:
    
    def __init__(self, num_nodes, edge_list, is_directed=False):
        
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
        
        self.is_directed = is_directed
        self.num_nodes   = num_nodes
        self.nodes = {}
        
        #Creo diccionario con listas vacias
        for i in range(num_nodes):
            self.nodes[i] = []
            
        #lleno el diccionario 
        for i,j in edge_list:
            if(is_directed == True):
                self.nodes[i].append(j)
            else:
                self.nodes[i].append(j)
                self.nodes[j].append(i)
                
        #Eliminar Repetidos
        for i in range (num_nodes):
            self.nodes[i] = list(dict.fromkeys(self.nodes[i]))  
