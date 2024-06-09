'''
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

'''

# Function for make_abba

def make_abba(a, b):
    return(a + b + b + a)

# Calling make_abba function with use cases

usecase_1 = make_abba('Hi', 'Bye')
usecase_2 = make_abba('Yo', 'Alice')
usecase_3 = make_abba('What', 'Up')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)