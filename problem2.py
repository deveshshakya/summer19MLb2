import numpy as np

for i in range(100, 125):
    j = i + 80
    mat = np.arange(i, j, 5).reshape(8, 2)
    print(mat)