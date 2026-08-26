import numpy as np  
import time


# (1) Measuring execution time, not a good method 

# start = time.time()
# for i in range(1,101):
#     print(i)

# print(time.time() - start)

# (2) Counting operations

def MySum(x):
    total = 0 
    for i in range(x+1):
        total+=i
    return total

# (3) Order of Growth

# BIG O Notation: O(n) - Linear Time Complexity
# count the operations 
def fact(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

# Number of operations 1 + 5n
# Remove additive constant = 5n(removed + 1)
# Remove multiplicative const = n (removed 5)

# Liner graph

# For example we have n^2  + 2n + 2
# n^2 tells that program has nested loop
# 2n: 2 operations in a loop
# 2: 2 operations outside the loop

# so, to calculate the time complexity of this eq.
# n^2 + n 
# We'll remove the smallent order  which is  n of order 1 

# n^2 