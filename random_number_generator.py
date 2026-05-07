import numpy as np
#integers random numbers
# rand=np.random.default_rng(seed=2)

# print(rand.integers(low=1,high=101,size=(5,4)))

#floating random number

# np.random.seed(seed=9)
# print(np.random.uniform(low=-1,high=6,size=(3,3)))

# RANDOM SHUFFLE
# rand=np.random.default_rng()
# arr=np.array([[1,2,3,4,5],
#              [6,7,8,9,10]])
# shape=arr.shape
# array=arr.flatten()
# np.random.shuffle(array)
# print(array.reshape(shape))

# CHOICE from array
rand=np.random.default_rng()
arr=np.array([1,2,3,4,5])
arrs=rand.choice(arr,size=2)
print(arrs)
