'''

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

'''

# Function for array123

def array123(nums):
    sublist = [1 , 2, 3]
    for i in range(len(nums)-2):
        if sublist == nums[i:i+3]:
            return True
    return False

# Calling array123 function with use cases

usecase_1 = array123([1, 1, 2, 3, 1])
usecase_2 = array123([1, 1, 2, 4, 1])
usecase_3 = array123([1, 1, 2, 1, 2, 3])

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)