'''

Given 2 strings, return their concatenation, except omit the first char of each.
The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

'''

# Function for non_start

def non_start(a, b):
    return(a[1:] + b[1:])
    

# Calling non_start function with use cases

usecase_1 = non_start('Hello', 'There')
usecase_2 = non_start('java', 'code')
usecase_3 = non_start('ab', 'x')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)