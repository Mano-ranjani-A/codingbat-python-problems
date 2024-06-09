'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'

'''

# Function for first_two

def first_two(str):
    if len(str) < 2:
        return str
    return(str[0:2])

# Calling first_two function with use cases

usecase_1 = first_two('Hello')
usecase_2 = first_two('abcdefg')
usecase_3 = first_two('a')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)