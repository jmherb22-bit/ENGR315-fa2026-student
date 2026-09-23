import random

# get a random integer between [0-10]
random_num = random.randint(0, 10)

# print out the number
print("The random number is: ", random_num)

# perform a single boolean test
if random_num == 2:
    print("The number is 2")

# combine two boolean tests
# only one needs to be true
if random_num == 2 or random_num < 5:
    print("Number is 2 or less than 5")

# combine two boolean tests
# both need to be true
if random_num < 2 and random_num < 5:
    print("Number is less than 2 and less than 5")

# if number is even
if random_num % 2 == 0:
    print("Value is even!")

# otherwise the value is odd
else:
    print("Value is odd!")

# is the number 5?
if random_num == 5:
    print("Value is 5!")

# maybe it's 4?
elif random_num == 4:
    print("Value is 4!")

# give up
else:
    print("I give up! It's not 4 or 5")


# let me find out what value we have
if random_num % 2 == 0:
    print("Value is even")

    if random_num == 4:
        print("Value is 4!")

        # now make the value odd
        random_num = random_num + 1

    else:
        print("Value is even and not 4!")

# if value is odd
elif random_num % 2 == 1:
    print("Value is odd!")

# this condition should never execute
else:
    print("We should never see this statement...")




