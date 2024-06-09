'''

Given a string, return a new string made of every other char starting with the first,
so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

'''

# Function for string_bits

def string_bits(str):
    result = ""
    for i in range(len(str)):
        if(i % 2 == 0):
            result = ''.join([result,str[i]])
    return result

# Calling string_bits function with use cases

usecase_1 = string_bits('Hello')
usecase_2 = string_bits('Hi')
usecase_3 = string_bits('Heeololeo')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)