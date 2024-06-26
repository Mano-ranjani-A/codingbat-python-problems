'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

'''

# Function for string_match

def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b))-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

# Calling string_match function with use cases

usecase_1 = string_match('xxcaazz', 'xxbaaz')
usecase_2 = string_match('abc', 'abc') 
usecase_3 = string_match('abc', 'axc')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)