
import numpy as np
from IPython.display import Math

class Pol1:
    
    def __init__(self):
        self.exps = []
        self.coefs = []
        
    def len(self):
        return len(self.exps)
        
    def add_term(self, c, e):
        
        i = np.searchsorted(self.exps, e)
        if i >= len(self.exps):
            self.exps.append(e)
            self.coefs.append(c)
        elif self.exps[i]==e:
            self.coefs[i] += c
        else:
            self.exps = self.exps[:i] + [e] + self.exps[i:]
            self.coefs = self.coefs[:i] + [c] + self.coefs[i:]
        assert len(self.exps)==len(self.coefs), "must have the same number of exps and coefs"
        return self

    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in zip(self.exps, self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)
