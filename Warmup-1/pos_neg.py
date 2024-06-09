'''
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

'''
# Function for pos_neg

def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return((a < 0 and b > 0 ) or (a > 0 and b < 0))
    
# Calling pos_neg function with use cases
    
usecase_1 = pos_neg(1, -1, False)
usecase_2 = pos_neg(-1, 1, False)
usecase_3 = pos_neg(-4, -5, True)

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)