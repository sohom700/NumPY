import numpy as np 
# ARRAY USE

# arr=np.array([1,2,3,4])
# arr*=2
# print(arr)

# N-D ARRAY 
arr = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
               [['J','K','L'],['M','N','O'],['P','Q','R']],
               [['S','T','U'],['V','W','X'],['Y','Z','?']]])
print(arr.ndim)
print(arr.shape)
print(arr[1,0,2]+arr[2,0,0]+arr[0,2,0])