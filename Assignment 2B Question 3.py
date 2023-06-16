# By Brett McDonald
# SID: 10158931
# Assignment 2B
# Question 3: A Tiny Editor

def positiveIntegerInput(input_message, error_custom_string = 'is not a valid input, please try again'): # this function will be used where positive integers are required as a strict user input
    '''This function is an alternative to the 'input()' function that will ensure that a positive integer is returned.
        This function may be called with an optional custom error string.'''
    while True:
        get_input = input(input_message)
        error_message = '{} {}'.format(get_input, error_custom_string)
        try:
            number = int(get_input)
            if number <= 0:
                print(error_message)
                continue
            return number
        except:
            print(error_message)

def fileNameInput(input_message, error_custom_string = 'is not a valid input, please try again'): # this function will be used where an appropriate file name is required as a strict user input
    '''This function is an alternative to the 'input()' function that will ensure that a suitable file name is returned (only alpha-numeric, '-', and '_' are allowed).
        This function may be called with an optional custom error string.'''
    while True:
        get_input = input(input_message)
        printError = False
        error_message = '{} {}'.format(get_input, error_custom_string)
        try:
            fileName = get_input
            for char in fileName:
                if char.lower() not in "abcdefghijklmnopqrstuvwxyz01234567890-_":
                    printError = True
            if printError:
                print(error_message)
                continue
            return fileName
        except:
            print(error_message)

listOfStrings = [] # initiate the list of strings

def commandPrompt():
    command = input('Command a, d, r, f, c, s, ?: ') # display the command prompt

    return command.lower()

while True:
    print("==============================") # add a line bar to differentiate input from output
    for index in range(len(listOfStrings)):
        print("{} ) {}".format((index+1),listOfStrings[index])) # format and display the list of strings

    cmd = commandPrompt() # assign the command

    if cmd == 'a': # action for command 'a' (add)
        while True:
            input_line = input("> ") # continuously prompt for user input
            if input_line != '#':
                listOfStrings.append(input_line) # add user input lines to the list of strings, except for the command '#'
            if input_line == '#':
                break # exit from the user_line input loop, return to the cmd = commandPrompt loop

    elif cmd == 'd': # action for command 'd' (delete a line)
        try: # prepare to catch index out of range error
            del_line = positiveIntegerInput("Delete line no: ") # prompt for a positive integer
            del listOfStrings[del_line-1] # delete the display number line (index-1) from the list of strings
            print("line {} deleted".format(del_line)) # display confirmation of the delete operation
        except:
            print("There are less than {} lines in the list".format(del_line)) # display message for index out of range

    elif cmd == 'r': # action for command 'r' (replace a line)
        try: # prepare to catch index out of range error
            replace_line = positiveIntegerInput("Replace line no: ") # prompt for a positive integer
            line_replacement = input("Replacement    : ") # prompt for a replacement
            listOfStrings[replace_line-1] = line_replacement
        except:
            print("There are less than {} lines in the list".format(replace_line)) # display message for index out of range

    elif cmd == 'f': # action for command 'f' (find and replace a string)
        find_string = input("Find string : ") # prompt for the search pattern
        replace_with = input("Replace with: ") # prompt for the replacement
        list_index = 0 # initiate the list index for searching through the list of strings
        while list_index < len(listOfStrings): # this is a safe method that allows for mutation of the list without going beyond the index range
            listOfStrings[list_index] = listOfStrings[list_index].replace(find_string,replace_with) # within the list of strings, all strings matching the search pattern are replaced with the replacement
            list_index += 1 # exit condition for the while loop

    elif cmd == 'c': # action for command 'c' (clear)
        del listOfStrings[:] # delete all lines in the list of strings

    elif cmd == 's': # action for command 's' (save)
        file_name = fileNameInput("Enter a file name (alphanumeric,dash and underscore only): ") # prompt for a file name
        fileWrite = open(file_name+".txt", 'w') # open a file for writing
        for line in listOfStrings:
            fileWrite.write(line+"\n") # write to the file all of the lines in list of strings
        fileWrite.close() # close the file

    elif cmd == '?': # action for command '?' (help)
        # display the help menu
        print("*** TinyEd commands ***")
        print("  a  Add - Start adding lines. A single # on a line by itself exits add.")
        print("  d  Delete a numbered line")
        print("  r  Replace a line")
        print("  f  Find & replace a string")
        print("  c  Clear")
        print("  s  Save")
        print("  q  Quit")

    elif cmd == 'q': # action for command 'q' (quit)
        break

# Sample Run Below:
# ==============================
# Command a, d, r, f, c, s, ?: ?
# *** TinyEd commands ***
#   a  Add - Start adding lines. A single # on a line by itself exits add.
#   d  Delete a numbered line
#   r  Replace a line
#   f  Find & replace a string
#   c  Clear
#   s  Save
#   q  Quit
# ==============================
# Command a, d, r, f, c, s, ?: a
# > It's a sunny day
# > and I've just had
# > lunc
# > #
# ==============================
# 1 ) It's a sunny day
# 2 ) and I've just had
# 3 ) lunc
# Command a, d, r, f, c, s, ?: r
# Replace line no: 3
# Replacement    : lunch.
# ==============================
# 1 ) It's a sunny day
# 2 ) and I've just had
# 3 ) lunch.
# Command a, d, r, f, c, s, ?: f
# Find string : day
# Replace with: afternoon
# ==============================
# 1 ) It's a sunny afternoon
# 2 ) and I've just had
# 3 ) lunch.
# Command a, d, r, f, c, s, ?: r
# Replace line no: 3
# Replacement    : a good lunch.
# ==============================
# 1 ) It's a sunny afternoon
# 2 ) and I've just had
# 3 ) a good lunch.
# Command a, d, r, f, c, s, ?: f
# Find string : u
# Replace with: UUU
# ==============================
# 1 ) It's a sUUUnny afternoon
# 2 ) and I've jUUUst had
# 3 ) a good lUUUnch.
# Command a, d, r, f, c, s, ?: f
# Find string : UUU
# Replace with: u
# ==============================
# 1 ) It's a sunny afternoon
# 2 ) and I've just had
# 3 ) a good lunch.
# Command a, d, r, f, c, s, ?: q
