'''

Given an int n, return the absolute difference between n and 21, except return double the absolute 
difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

'''
# Function for diff21
def diff21(n):
    if n > 21:
        return(abs(n - 21) * 2)
    else:
        return(abs(n - 21))
    
# Use cases
usecase_1 = diff21(35)
usecase_2 = diff21(19)
usecase_3 = diff21(21)

# Printing all test cases
print(usecase_1, usecase_2, usecase_3)