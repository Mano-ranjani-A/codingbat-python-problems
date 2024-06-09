'''

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

# Function for last2

def last2(str):
  substr = str[-2:]
  count = 0
  if len(str) <= 1:
    return count
  else:
    for i in range(len(str)-1):
        result = str[i] + str[i+1]
        if result == substr:
            count += 1
    return (count - 1)

# Calling last2 function with use cases

usecase_1 = last2('hixxhi')
usecase_2 = last2('xaxxaxaxx')
usecase_3 = last2('axxxaaxx')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)