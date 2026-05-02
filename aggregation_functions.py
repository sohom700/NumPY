import numpy as np

arr=np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmax(arr))
# print(np.argmin(arr))
# print(np.std(arr))

# for sum of column axis = 0 and for sum of row axis will be = 1

print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
