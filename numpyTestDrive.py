import numpy as np
matrix = [[[[(1,2,3),(4,5,6)],[(3,2,3),(4,5,3)]],[[(1,2,3),(4,5,6)],[(3,2,3),(4,5,3)]]],[[[(1,2,3),(4,5,6)],[(3,2,3),(4,5,3)]],[[(1,2,3),(4,5,6)],[(3,2,3),(4,5,3)]]]]
rayales = np.array(matrix)
print(rayales)
print('shape')
print(rayales.shape)
print('ndim')
print(rayales.ndim)
print('item size')
print(rayales.itemsize)
