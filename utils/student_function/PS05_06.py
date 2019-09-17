from PS05 import *
class L6(L):
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        nodo_mio  = self.first_node
        nodo_tuyo = other.first_node
        for i in range(len(self)):
            if nodo_mio.value != nodo_tuyo.value:
                return False
            else:
                nodo_mio  = nodo_mio.next 
                nodo_tuyo = nodo_tuyo.next
        
        return True
    
    def __ne__(self, other):
        return not self==other       
