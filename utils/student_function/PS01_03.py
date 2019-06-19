

def append(l,d):
    l += [d]
    return l

def getremove_last(l):
    assert len(l) > 0, "AssertionError"
    longitud = len(l)
    val = l[longitud -1]
    rest_list = l[:-1]
    return val, rest_list  

class Stack:
    
    def __init__(self):
        self.elements = []
  
    def put(self, d):
        self.elements.append(d)
        return self
        
    def get(self):
        assert len(self.elements) > 0, "No hay nada en la pila"
        return self.elements.pop()

    def len(self):
        return len(self.elements)

