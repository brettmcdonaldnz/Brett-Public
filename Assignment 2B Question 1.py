# By Brett McDonald
# SID: 10158931
# Assignment 2B
# Question 1: Currency Conversion Table

conversionRate = {"NZ$":1, "AUD":0.96, "USD":0.75, "EURO":0.67, "GBP":0.496}
amounts = [10,20,30,40,50,60,70,80,90,100]

currencies = ["NZ$", "AUD", "USD", "EURO", "GBP"]

for amount in amounts:
    rowString = ''
    for currency in currencies:
        rowString += "{} {:>6.2f}    ".format(currency, (amount * conversionRate[currency]))
    print(rowString)
