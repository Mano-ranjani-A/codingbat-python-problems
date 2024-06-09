'''


Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'

'''

# Function for left2

def left2(str):
    return(str[2:] + str[:2])
    

# Calling left2 function with use cases

usecase_1 = left2('Hello')
usecase_2 = left2('java')
usecase_3 = left2('ab')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)