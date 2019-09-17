import PS06
class VBinTree(PS06.VBinTree):
        
    def get_last_parent_position(self):
        ultimo_hijo = len(self.v)-1 if self.v[-1] is not None else len(self.v)-2
        ultimo_padre = self.get_parent_position(ultimo_hijo)
        return ultimo_padre
