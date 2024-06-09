'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''

# Function for missing_char

def missing_char(str, n):
    return(str[:n]+str[n+1:])

# Calling missing_char function with use cases
    
usecase_1 = missing_char('candy', 0)
usecase_2 = missing_char('x', 1)
usecase_3 = missing_char('not bad', 4)

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)