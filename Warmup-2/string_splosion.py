'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

'''

# Function for string_splosion

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

# Calling string_splosion function with use cases

usecase_1 = string_splosion('Hello')
usecase_2 = string_splosion('Hi')
usecase_3 = string_splosion('Heeololeo')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)