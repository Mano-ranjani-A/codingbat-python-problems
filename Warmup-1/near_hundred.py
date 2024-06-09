'''
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

'''

# Function for near_hundred

def near_hundred(n):
    return((abs(n - 100) <= 10 or abs(n-200) <= 10))

# Use cases

usecase_1 = near_hundred(93)
usecase_2 = near_hundred(90)
usecase_3 = near_hundred(89)

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)