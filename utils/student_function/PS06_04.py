import PS06
class VBinTree(PS06.VBinTree):

    def shift_down(self, start, end=None): 
        end = len(self.v)-1 if end is None else end
        root = start
        while self.get_children_positions(root)[0] is not None and self.get_children_positions(root)[0]<=end:
            a,b  = self.get_children_positions(root)
            mayor = a if self.v[a] > self.v[root] else root
            if b is not None:
                mayor = mayor if self.v[mayor] > self.v[b] else b
            if mayor == root:
                return self
            self.v[mayor],self.v[root] = self.v[root],self.v[mayor]
            root = mayor
        return self
        
    def get_last_parent_position(self):
        ultimo_hijo = len(self.v)-1 if self.v[-1] is not None else len(self.v)-2
        ultimo_padre = self.get_parent_position(ultimo_hijo)
        return ultimo_padre
    
    def make_heap(self):
        ultimo_padre = self.get_last_parent_position()
        for i in reversed(range(int(ultimo_padre +1))):
            self.shift_down(i)
    
    def sort(self):
        self.v.sort()
