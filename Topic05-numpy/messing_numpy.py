# Learning numpy again...
# Author: Andre

import numpy as np

a = np.array([1, 2, 3]) # create a rank 1 array

# creating an array
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5            # change an element of the array
print(a)

# creating a 2 dimension array
b = np.array([[1,2],[3,4]]) # create a rank 2 array
print(b)

print(b.shape) # shape shows the array numbers quantity

a = np.zeros((2,2)) # create an array of all zeros
print(a)

b = np.ones((1,2)) # create an array of all ones
print(b)

c = np.full((2,2), 7) # create a constant array
print(c)

d = np.eye(2) # Create a 2x2 identity array
print(d)

e = np.random.random((2,2)) # create an array filled with random values
print(e)

f = np.arange(10,50,5) # create an array of values starting at 10 in increments of 5
print(f)

g = np.linspace(0., 1., num=5) # create an array with values starting at 0 until 1 with range of 5 numbers
print(g)

# building an array from existing array by stacking them vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))

# building an array from existing array by horizontally
a = np.array([[7], [8], [9]])
b = np.array([[4], [5], [6]])
print(np.hstack((a,b)))

# create the following rank 2 array with shape (3,4)
# [[1 2 3 4]
#  [5 6 7 8]
#  [9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
# use slicing to pull out the subarray of the first 2 rows and columns
# 1 and 2; b is the following array of shape (2,2)
b = a[:2, 1:3]
print(b)

# 2 ways fo accessing the data in the middle row fo the array
row_r1 = a[1, :]
row_r2 = a[1:2, :]
row_r3 = a[[1], :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)