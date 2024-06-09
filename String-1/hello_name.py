'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

'''

# Function for hello_name

def hello_name(name):
    return("Hello " + name + "!")

# Calling hello_name function with use cases

usecase_1 = hello_name('Bob')
usecase_2 = hello_name('Alice')
usecase_3 = hello_name('X')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)