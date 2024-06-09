'''

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

'''

# Function for parrot_trouble

def parrot_trouble(talking, hour):
    if (talking == True) and (hour < 7 or hour > 20):
        return True
    else:
        return False
    
# Alternate solution
def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))


# Use cases
    
usecase_1 = parrot_trouble(True, 6)
usecase_2 = parrot_trouble(True, 7)
usecase_3 = parrot_trouble(False, 6)

# Printing 

print(usecase_1, usecase_2, usecase_3)


