'''

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

'''

# Function for combo_string

def combo_string(a, b):
    return(min(a, b, key = len) + max(a, b, key = len) + min(a, b, key = len))

# Calling combo_string function with use cases

usecase_1 = combo_string('Hello', 'hi')
usecase_2 = combo_string('hi', 'Hello')
usecase_3 = combo_string('aaa', 'b')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)