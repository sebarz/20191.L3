import PS07
class BTNode(PS07.BTNode):
    
    def height(self):
        if self.value == None:
            return - 1
        h1 = self.left.height() if self.left is not None else -1
        h2 = self.right.height() if self.right is not None else -1
            
        return max(h1,h2)+1

    def balance_factor(self):
        h1 = self.right.height() if self.right != None else -1
        h2 = self.left.height() if self.left != None else -1       
        return h2-h1
        
        return result
    
    def balance_factor_tree(self):
        r = self.__class__(self.balance_factor(), \
                           left=self.left.balance_factor_tree() if self.left is not None else None,
                           right=self.right.balance_factor_tree() if self.right is not None else None,
                          )
        return r
    
    def rotate_left(self):
        
        assert self.balance_factor() == -2 and self.right.balance_factor() == -1, "invalid balance factor"
        copy = self.clone()
        p , q = copy, copy.right
        p.right, q.left = q.left, p
        
        return q
