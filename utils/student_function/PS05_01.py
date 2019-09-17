from PS05 import *
class L1(L):
    def __getitem__(self, idx):
        idx = idx if idx>=0 else len(self) - abs(idx)
        k = self.first_node
        for i in range(idx):
            assert k.next is not None, "index %s out of range""%(str(idx))"
            k = k.next
            
        return k.value
