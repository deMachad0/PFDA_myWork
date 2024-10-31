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

# 2 ways fo accessing the data in the middle row of the array
row_r1 = a[1, :]
row_r2 = a[1:2, :]
row_r3 = a[[1], :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)

# making the same distinction when accessing columns
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

# create a new array which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(a)

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of using the indice in b
print(a[np.arange(4), b])
print()
# mutate one element from each row of a using the indice in b
a[np.arange(4), b] += 10
print(a)

# boolean array indexing: pick elements of an array to satisfy some condition
a = np.array([[1,2], [3,4], [5,6]])

bool_idx = (a > 2) # finds an element of a that are bigger than 2
                   # this returns a boolean
print(bool_idx)

# we can take the values of the original array and print it 
print(a[bool_idx])
# we can also do all the above in a concise way
print(a[a > 2])
print()

# some useful functions to be used: argmax (get the maximum element), argmin (get the minimun element)
# argsort (get sorted list of indices, by element value, in ascending)
# where (get indices of elements that meet some condition)
a = np.array([1, 8, 9, -3, 2, 4, 7, 9])
print(np.argmax(a)) # index maximum
print(np.argmin(a)) # index minimun
print(np.argsort(a))
# get sorted list of indices in descending order
print(np.argsort(a)[:: -1])
# this returns a tuple, the list of indices is the first entry, use [0]
print(np.where(a > 5)[0])

# this example shows how to get te index of all the max values
print(np.where(a >= a[np.argmax(a)])[0])

# Array math
# creating an array using random
a = np.random.random(100000000)
print(a)
# seing the time spent to sum all array
#%%time 
x = np.sum(a) # takes less time
# seing the time spent to sum all array using for 
#%%time 
x = 0
for element in a:
    x = x + element # takes too much time

# adding arrays together
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

print(x + y)
print(np.add(x, y))