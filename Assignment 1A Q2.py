# BRETT MCDONALD
# SID 10158931
# Assignment 1A
# Question 2: Write a string length calculator (6 marks)
# a) Write a function that builds a list of strings from user input.

def build_string_list():
    number_of_strings = int(input("How many items do you want in your list? "))
    new_list = []
    string_list_number = 0
    for string in range(number_of_strings):
        string_list_number += 1
        new_list.append(input("Enter string "+str(string_list_number)+": "))
    print(new_list)
    return new_list

build_string_list()

# OUTPUT
# How many items do you want in your list? 4
# Enter string 1: banana
# Enter string 2: orange
# Enter string 3: apple
# Enter string 4: plum
# ['banana', 'orange', 'apple', 'plum']

# b) Write another function that calculates the total length of all strings in a list.

def length_of_all_strings(list):
    total_length = 0
    for string in list:
        print("The length of the string '"+string+"' is:", len(string))
        total_length += len(string)
    print("The total length of all strings is:",total_length)

length_of_all_strings(build_string_list())

# OUTPUT
# How many items do you want in your list? 4
# Enter string 1: banana
# Enter string 2: orange
# Enter string 3: apple
# Enter string 4: plum
# ['banana', 'orange', 'apple', 'plum']
# The length of the string 'banana' is: 6
# The length of the string 'orange' is: 6
# The length of the string 'apple' is: 5
# The length of the string 'plum' is: 4
# The total length of all strings is: 21
