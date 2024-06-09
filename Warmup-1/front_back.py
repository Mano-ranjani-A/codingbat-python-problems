'''

Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''

# Function for front_back

def front_back(str):
    if len(str)<=1:
        return (str)
    return(str[-1] + str[1:-1] + str[0])

    
# Calling front_back function with use cases
    
usecase_1 = front_back('candy')
usecase_2 = front_back('x')
usecase_3 = front_back('')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)