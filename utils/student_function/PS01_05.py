import numpy as np
def fill(t, n):
    numeros = np.random.randint(10,size=n)
    for i in numeros: 
        t.put(i)
    return t
