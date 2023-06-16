# BRETT MCDONALD
# SID 10158931
# Assignment 1B
# Question 2: Build a list of multiples and calculate the product (6 marks)
#
# a) Write a function that returns a list of numbers that are multiples of a specified number.


def multiples_of_list():
    multiple_of = int(input("Multiples of: "))
    limit = int(input("Enter an upper limit: "))
    list_of_multiples = []
    for number in range(multiple_of, limit+1, multiple_of):
        list_of_multiples.append(number)
    return list_of_multiples

print(multiples_of_list())

# # RESULT:
# Multiples of: 2
# Enter an upper limit: 10
# [2, 4, 6, 8, 10]

# b) Write another function that takes a list of numbers as a parameter and calculates the product of all the items in the list

def product_of_list():
    multiplicand = 1
    list = multiples_of_list()
    for number in list:
        multiplicand *= number
    return "{0}\nThe product of the list {0} is: {1}".format(list, multiplicand)

print(product_of_list())

# RESULT
# Multiples of: 2
# Enter an upper limit: 10
# [2, 4, 6, 8, 10]
# The product of the list [2, 4, 6, 8, 10] is: 3840
