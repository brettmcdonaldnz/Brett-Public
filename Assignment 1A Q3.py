# BRETT MCDONALD
# SID 10158931
# Assignment 1A
# Question 3: Write a program to play the Mad Libs Game (6 marks)

def mad_libs():
    print("    Welcome to Mad Libs!")
    print("    Please provide the following to help")
    print("    create a new story")
    name = input("Enter a name:")
    noun = input("Enter a plural noun:")
    int_value = input("Enter an integer value:")
    body_part = input("Enter a body part:")
    verb = input("Enter a verb:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Here is your story")
    print("The famous explorer",name,"had nearly given up a life long quest to find")
    print("the lost city of",noun,"when one day, the",noun,"found the explorer.")
    print("Surrounded by",int_value,noun+", a tear came to",name+"'s",body_part+".")
    print("After all this time, the quest was finally over.")
    print("And then, the",noun,"promptly devoured",name+".")
    print("The moral of the story? Be careful what you",verb,"for.")
    print("~~~~~~~~~~~~~~~~The end~~~~~~~~~~~~~~~~~~~~")

mad_libs()

# OUTPUT
#     Welcome to Mad Libs!
#     Please provide the following to help
#     create a new story
# Enter a name:Brett
# Enter a plural noun:assignments
# Enter an integer value:4
# Enter a body part:eye
# Enter a verb:enrol
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here is your story
# The famous explorer Brett had nearly given up a life long quest to find
# the lost city of assignments when one day, the assignments found the explorer.
# Surrounded by 4 assignments, a tear came to Brett's eye.
# After all this time, the quest was finally over.
# And then, the assignments promptly devoured Brett.
# The moral of the story? Be careful what you enrol for.
# ~~~~~~~~~~~~~~~~The end~~~~~~~~~~~~~~~~~~~~
