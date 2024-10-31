# Learning random number generation
# Author: Andre

import numpy as np
import matplotlib.pyplot as plt

# generate random numbers from an uniform distribution
random_gnr = np.random.uniform(low=0, high=1, size=10)
print(random_gnr)

# generate random numbers
x = np.random.uniform(low=0, high=1, size=1000)
plt.hist(x) # putting the random numbers into a histogram
plt.show()
print()

# to simulate an unfair coin
size = 20
x = np.random.uniform(low=0, high=1, size=size)

# make the coin flips (< 0.7 means we have a 70% chance of heads)
heads = x < 0.7

# show which were heads, and count the number of heads
print(heads)
heads_count = heads.sum() # or np.sum(heads)
tails_count = size - heads_count
print(f"\nThere were {heads_count} heads. (and {tails_count} tails.)")
# putting into a pie graphic
labels = ["heads", "tails"]
plt.pie(np.array([heads_count, tails_count]), labels = labels)
plt.show()

# another tool to generate random numbers
rng = np.random.default_rng(seed=3252) # seed will guarantee the exactly same numbers
# draw random numbers
print(rng.uniform(size=10))

rng = np.random.default_rng(seed=3252) # seed will guarantee the exactly same numbers
# draw random numbers
print(rng.uniform(size=10))

rng = np.random.default_rng(seed=3253) # seed is different now, generating other numbers
# draw random numbers
print(rng.uniform(size=10))

# Drawing random numbers out of other distribution
# set parameters
mu = 10
sigma = 1
# draw 100000 random samples
x = rng.normal(mu, sigma, size=10000)

plt.hist(x, bins=1000)
plt.show()

# draw how many coin flips land heads in 10 files
print(rng.binomial(10, 0.5))
print()

# Choosing elements from an array
# rng.choice() function (replace= parameter allows you to specify if the same entry
#can be draw twice
rng = np.random.default_rng(seed=126969234)
print(rng.integers(0, 51, size=20))

print(rng.choice(np.arange(51), size=20, replace=False)) # because replace=False we dont get any repeats
print()
# shuffling an array
print(rng.permutation(np.arange(53)))
