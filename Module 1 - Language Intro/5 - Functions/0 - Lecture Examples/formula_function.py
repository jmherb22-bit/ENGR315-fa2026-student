def compound_return(initial_investment, interest_rate, years):
    """
    Calculate the total return on an investment that compounds annually
    :param initial_investment: Initial principal investment
    :param interest_rate: Rate of return expressed as an integer between 0 and 100
    :param years: Number of years to hold the investment
    :return: Total value of the investment at the end of the term
    """
    final_value = initial_investment * (1 + (interest_rate / 100)) ** years

    return final_value


principal = 1000  # initial amount to be deposited
rate = 1  # interest rate applied to deposit (will be divided by 100)
n = 10  # number of years to compound deposit

# must cast n as 'string' so it can be printed in print()
print("Initial principal is $" + str(principal))
print("Interest rate is " + str(rate / 100))
print("Hold for " + str(n) + " years")

# calculate the eventual result
final = compound_return(principal, rate, n)

# fancy print the output with two decimal places for floating number
print(f"Final value after is ${final:.2f}")


