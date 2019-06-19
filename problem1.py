import numpy as np

while True:
    dim = input("Enter Dimension : ")
    r, c = int(dim[0]), int(dim[2])
    arr = np.random.randn(r, c)
    print(arr)
    print()
    with open('array.txt', 'a') as f:
        f.write(str(arr))
