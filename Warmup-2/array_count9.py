'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

'''

# Function for array_count9

def array_count9(nums):
    return(nums.count(9))

# Calling array_count9 function with use cases

usecase_1 = array_count9([1, 2, 9])
usecase_2 = array_count9([1, 9, 9])
usecase_3 = array_count9([1, 9, 9, 3, 9])

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)