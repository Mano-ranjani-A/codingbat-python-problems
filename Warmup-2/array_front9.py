'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

'''

# Function for array_front9

def array_front9(nums):
    return(9 in (nums[:4] or nums[:]))

# Calling array_front9 function with use cases

usecase_1 = array_front9([1, 2, 9, 3, 4])
usecase_2 = array_front9([1, 2, 3, 4, 9])
usecase_3 = array_front9([1, 2, 3, 4, 5])

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)