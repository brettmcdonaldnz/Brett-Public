# By Brett McDonald
# SID: 10158931
# Assignment 3
# Question 1: Random Sentence Generator

import random


def get_menu_option():
    """displays a menu and carries out the appropriate action depending on which letter the user types, and then re-displays the menu"""

    print('*** Random Sentence Generator ***')
    print('   L - Load - load all the files of words from disk')
    print('''   T - Test - display the first word from each list to make sure they've been loaded''')
    print('   E - Easy sentence - display a two word sentence')
    print('   S - New sentence - generate & display a sentence conforming to the grammar algorithm')
    print('   Q - Quit - quit the program')
    command = input('command: ?')
    print()

    return command.upper()


def load():
    """load each of the files of words from disk into a global dictionary"""

    global grammar_dictionary                                                       # initiate the grammar dictionary as a global variable
                                                                                    # all grammar file names are contained in the list below
    fileList = [
        "Adjectives","Adverbs","Conjunctions",
        "IntransitiveVerbs","Leadin","NounMarkers",
        "Nouns","TransitiveVerbs"
    ]

    grammar_dictionary = {}                                                         # initiate the grammar dictionary global variable as a dictionary
    for fileName in fileList:                                                       # iterate over each file name in the file list
        grammar_dictionary.update({fileName:open("{}.txt".format(fileName),"r")})   # assign each file name as a key, and the value of each key as opening that file for reading
    for file in grammar_dictionary.values():
        print("loaded {}".format(file.name))                                        # display the name of each file opened
    print()


def test():
    """display the first word from each list to make sure they've been loaded"""

    try:                                                        # check if the grammar dictionary has been loaded
        print("Testing files...")
        for file in grammar_dictionary.values():                # iterate over each file loaded
            first_line = file.readline()                        # read the first line in each file
            first_word = first_line.split()[0]                  # read the first word in the first line of each file
            print("{}... from {}".format(first_word,file.name)) # display the first word in the first line of each file, and the name of the file it came from
        print()
    except:
        print("The grammar dictionary has not been loaded")
        print()


def rand_element(filename):
    """generate a string from a random line in a named file that was previously loaded into the grammar dictionary by load()"""

    listLines = []
    for line in grammar_dictionary[filename].readlines():
        listLines.append(line.strip())                      # add each line in the file to the list of elements, and strip the trailing \n
    grammar_dictionary[filename].seek(0)                    # reset the read cursor position to the beginning for the next time the function is called
    randIndex = random.randrange(len(listLines))            # generate a random index encompassing the element list range
    randomElement = listLines[randIndex]                    # generate a random element as a string variable
    return randomElement


def capitalise_string_first_word(inputString):
    """Capitalise the first element of a string without lower-casing the rest of the string (as would occur if .capitalized() is used)"""

    stableString = inputString                                                      # ensures that if the input string is a random string generator function, that input function is only called once
    outputString = ''
    if len(stableString.split()) > 1:                                               # if there is more than one word in the string...
        for word in stableString.split():                                           # iterate over each word in the string...
            if stableString.split().index(word) == 0:                               # for the first word in the string...
                outputString += word.capitalize() + " "                             # capitalise the first word in the string, add a space, and add it to the capitalised output string
            elif stableString.split().index(word) == len(stableString.split())-1:   # if it is the last word in the string...
                outputString += word                                                # no space is added to the last word in the string
            else:
                outputString += word + " "                                          # all the middle words in the string are added to the output string, with a space and no other changes
    else:
        outputString += stableString.capitalize()                                   # if the input string only has one word, capitalise it
    return outputString


def noun_phrase():
    """Generate a phrase comprising a random noun-marker, an optional random adjective (incl 50% of the time), and a random noun """

    nounPhraseOption = random.choice([1,2])
    if nounPhraseOption == 1:       # option including random adjective
        nounPhrase = "{} {} {}".format(rand_element("NounMarkers"),rand_element("Adjectives"),rand_element("Nouns"))
    elif nounPhraseOption == 2:     # option excluding random adjective
        nounPhrase = "{} {}".format(rand_element("NounMarkers"),rand_element("Nouns"))
    return nounPhrase


def verb_phrase():
    """Generate a phrase comprising either a random intransitive verb (50% of the time), or a transitive verb followed by a noun phrase (50% of the time)"""

    verbPhraseOption = random.choice([1,2])
    if verbPhraseOption == 1:       # option with just an intransitive verb
        verbPhrase = rand_element("IntransitiveVerbs")
    elif verbPhraseOption == 2:     # option with a transitive verb and a noun phrase
        verbPhrase = "{} {}".format(rand_element("TransitiveVerbs"),noun_phrase())
    return verbPhrase


def easy_sentence():
    """display a two word sentence - a randomly selected noun followed by a randomly selected intransitive verb and then a full stop"""

    try:
        if grammar_dictionary:      # check if the grammar dictionary has been loaded
            sentence = "{} {}.".format(capitalise_string_first_word(rand_element("Nouns")),rand_element("IntransitiveVerbs"))
            print(sentence)
            print()
    except:
        print("The grammar dictionary has not been loaded")
        print()


def new_sentence():
    """generate & display a sentence conforming to the grammar algorithm. Display an error message if the word lists haven't been loaded"""

    try:
        if grammar_dictionary:
            sentenceOption = random.choice([1,2,3,4])
            if sentenceOption == 1:     # option with lead-in and adverbs included
                sentence = "{} {} {} {}.".format(capitalise_string_first_word(rand_element("Leadin")),noun_phrase(),rand_element("Adverbs"),verb_phrase())
            elif sentenceOption == 2:   # option with lead-in and adverbs excluded
                sentence = "{} {}.".format(capitalise_string_first_word(noun_phrase()),verb_phrase())
            elif sentenceOption == 3:   # option with lead-in included, adverbs excluded
                sentence = "{} {} {}.".format(capitalise_string_first_word(rand_element("Leadin")),noun_phrase(),verb_phrase())
            elif sentenceOption == 4:   # option with lead-in excluded, adverbs included
                sentence = "{} {} {}.".format(capitalise_string_first_word(noun_phrase()),rand_element("Adverbs"),verb_phrase())
            print(sentence)
            print()
    except:
        print("The grammar dictionary has not been loaded")
        print()


def quit_program():
    """quit the program"""

    try:                                            # check if the grammar dictionary has been loaded
        for file in grammar_dictionary.values():
            file.close()
            print("Closed {}".format(file.name))    # display the name of each file closed
        print('Quitting program...')
    except:
        print('Quitting program...')


while True:
    cmd = get_menu_option() # Display the menu and return a valid option
    if cmd == 'L':          # Load - load all the files of words from disk
        load()
    elif cmd == 'T':        # Test - display the first word from each list to make sure they've been loaded
        test()
    elif cmd == 'E':        # Easy sentence - display a two word sentence - a randomly selected noun followed by a randomly selected intransitive verb and then a full stop
        easy_sentence()
    elif cmd == 'S':        # New sentence - generate & display a sentence conforming to the grammar algorithm. Display an error message if the word lists haven't been loaded.
        new_sentence()
    elif cmd == 'Q':        # Quit - quit the program
        quit_program()
        break


input('')
