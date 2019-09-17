def PriorityQueue():
    class _PriorityQueue:
        def __init__(self):
            self.items = []
            self.priority = []
            
        def empty(self):
            return True if len(self.elements) == 0 else False

        def put(self, item, priority):
            self.items.append(item)
            self.priority.append(priority)

        def get(self):
            idx_menor = self.priority.index(min(self.priority))
            menor = self.priority.index(self.items[idx_menor])
            self.items.remove(menor)
            self.priority.remove(menor)
            return menor
        
    return _PriorityQueue()
