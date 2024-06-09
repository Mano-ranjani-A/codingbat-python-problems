'''

Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''

# Function 

def not_string(str):
    if (str.startswith("not")):
        return str
    return(''.join(["not ",str]))

    
# Calling not_string function with use cases
    
usecase_1 = not_string('candy')
usecase_2 = not_string('x')
usecase_3 = not_string('not bad')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)