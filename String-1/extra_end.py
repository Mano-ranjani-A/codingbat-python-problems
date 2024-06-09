'''

Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'

'''

# Function for extra_end

def extra_end(str):
    return(str[-2:]*3)


# Calling extra_end function with use cases

usecase_1 = extra_end('Hello')
usecase_2 = extra_end('ab')
usecase_3 = extra_end('Hi')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)