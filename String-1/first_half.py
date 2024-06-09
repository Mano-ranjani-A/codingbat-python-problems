'''

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

'''

# Function for first_half

def first_half(str):
    return(str[:len(str)//2])

# Calling first_half function with use cases

usecase_1 = first_half('WooHoo')
usecase_2 = first_half('HelloThere')
usecase_3 = first_half('abcdef')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)