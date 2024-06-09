'''

Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

'''

# Function for string_times

def string_times(str, n):
    return(str * n)

# Calling string_times function with use cases

usecase_1 = string_times('candy', 0)
usecase_2 = string_times('x', 1)
usecase_3 = string_times('not bad!', 4)

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)