import numpy as np
def find_target(grid):
    laberinto = np.array(grid)
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == "T":
                target = i,j
                return target
