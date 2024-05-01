import numpy as np

i= np.array([[1,2,3],[11,8,9]])
j= np.array([[2,5,6],[6,7,8]])

dot_pdt = sum(i*j)
print("The element-wise multiplication of A & B is {}".format(dot_pdt))
