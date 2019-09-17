from PS05 import *
class L4(L):
    def __setitem__(self, idx, value):
            assert idx<len(self) and idx>(-len(self)-1), "malo"
            id=idx%len(self)
            k=self.first_node
            for i in range(id):
                k=k.next
            k.value=value
    
    
    def clone(self):
        def clone_node(node):
            if node is None:
                return None
            else:
                r=Node(node.value,clone_node(node.next))
                return r
        
            
        w=Node(self.first_node.value,clone_node(self.first_node.next))
        m=L4(w)
        for i in range(len(m)):
            if isinstance(m[i],type(m))==True:
                u=m[i].clone()
                m[i]=u
            
        
        return m
