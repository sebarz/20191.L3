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
