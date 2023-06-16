# BRETT MCDONALD
# SID 10158931
# Assignment 1A
# Question 1: Write a savings calculator (3 marks)

def savings_calc(amount, number_of_weeks):
    savings = amount * number_of_weeks
    string = "You can save a total of $"+str(savings)+" over "+str(number_of_weeks)+" weeks."
    return string

weekly_savings = float(input("Enter the amount of money you can save per week (do not include the '$' sign): "))
weeks_of_savings = int(input("Enter the number of weeks you want to save for (must be a whole number): "))

result = savings_calc(weekly_savings, weeks_of_savings)
print(result)

# OUTPUT
# Enter the amount of money you can save per week (do not include the '$' sign): 50.45
# Enter the number of weeks you want to save for (must be a whole number): 55
# You can save a total of $2774.75 over 55 weeks.

