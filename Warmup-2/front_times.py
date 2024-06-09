'''

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

'''

# Function for front_times

def front_times(str, n):
    if len(str) < 3:
        return str*n
    return (str[:3] * n)

# Calling front_times function with use cases

usecase_1 = front_times('candy', 0)
usecase_2 = front_times('x', 1)
usecase_3 = front_times('not bad!', 4)

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)