'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

'''

# Function

def makes10(a, b):
  return ((a + b == 10) or (a == 10 or b ==10))

# Use cases

usecase_1 = makes10(9, 10)
usecase_2 = makes10(9, 9)
usecase_3 = makes10(1, 9)

# Printing all use-cases

print(usecase_1, usecase_2, usecase_3)