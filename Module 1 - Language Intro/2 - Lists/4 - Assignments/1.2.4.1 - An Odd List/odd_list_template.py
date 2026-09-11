import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""
# randomly sample a distribution between 1 and 5
random_number = int(random.uniform(1, 5))

# any number times 2 is even, add one to make it odd
an_odd_number = 2 * random_number + 1

# generate a random list of odd length containing values up to 100
odd_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", odd_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

# use len() to find the length of the list
list_length = len(odd_list) #modify this line to perform the correct operation

# now calculate the middle index of the list
middle_index = list_length // 2 #modify this line to perform the correct operation

# use [] to access the middle element. Set it equal to middle_element
middle_element = odd_list[middle_index] #modify this line to perform the correct operation

# print out the middle_element
print("The middle element is: ", middle_element)
