# BRETT MCDONALD
# SID 10158931
# Assignment 1B
# Question 1: Write an investment calculator (3 marks)

# Compound interest formula:
# S = P * (1+ (j/n)) ** (n * t)

def investment_calc():
    P = float(input("Enter the initial value of the investment: "))
    j = float(input("Enter the interest rate: ")) # use a decimal value, e.g. 5% = 0.05
    t = float(input("How many years will the amount be invested for? "))
    total_return = float(P * (1+ (j/12)) ** (12 * t))
    return "The final value of your invesment after 10 years is ${0:.2f}".format(total_return)

print(investment_calc())

# RESULT
# Enter the initial value of the investment: 5000
# Enter the interest rate: 0.05
# How many years will the amount be invested for? 10
# The final value of your invesment after 10 years is $8235.05
