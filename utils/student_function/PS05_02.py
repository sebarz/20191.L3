from PS05 import *
class L2(L):
    def __setitem__(self, idx, value):
        idx = idx if idx>=0 else len(self) - abs(idx)
        k = self.first_node
        for i in range(idx):
            assert k.next is not None, "index %s out of range""%(str(idx))"
            k = k.next
            
        k.value = value
