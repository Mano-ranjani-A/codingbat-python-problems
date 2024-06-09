'''

Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

'''

# Function for front3

def front3(str):
  if(len(str) < 3):
    return str * 3
  return(str[:3]*3)

# Calling front3 function with use cases
    
usecase_1 = front3('candy')
usecase_2 = front3('x')
usecase_3 = front3('')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)