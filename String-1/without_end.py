'''
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'

'''

# Function for without_end

def without_end(str):
    return(str[1:-1])
    

# Calling without_end function with use cases

usecase_1 = without_end('WooHoo')
usecase_2 = without_end('HelloThere')
usecase_3 = without_end('ab')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)