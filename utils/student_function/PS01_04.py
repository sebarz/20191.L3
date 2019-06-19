

def append(l,d):
    l += [d]
    return l


class Queue:
    
    def __init__(self):
        self.elements = []
        
    def put(self, d):
        self.elements.append(d)
        return self
    
    def get(self):
        assert len(self.elements) > 0, "cola vacía"
        val = self.elements[0]
        self.elements = self.elements[1:]
        return val
    
    def len(self):
        return len(self.elements)
