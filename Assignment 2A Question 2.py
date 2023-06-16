# By Brett McDonald
# SID: 10158931
# Assignment 2A
# Question 2: A Movie Title Explorer

import random

file = open("movies.txt", "r") # open the movie file
movies_list = file.readlines() # load each line into a list
file.close() # close the file

movies_list = [ movie.strip() for movie in movies_list ] # remove the \n at the end of each line
print(len(movies_list),'movies loaded\n')

output_log = [] # this will be used for logging displayed movies, and facilitates the 'save' function
my_favourites_list = [] # the 'save' function will append output_log to the favourites list


def get_menu_option():
    '''displays a menu and carries out the appropriate action depending on
        which letter the user types, and then re-displays the menu'''

    print('*** Movie Title Explorer ***')
    print('   r - random movie')
    print('   b - begins with')
    print('   f - find')
    print('   s - save the last displayed movie title to your favourites')
    print('   m - my favourites display')
    print('   c - clear favourites')
    print('   q - quit')
    command = input('command: ?')
    print()

    return command.lower()

def random_movie():
    '''Randomly pick a movie title and display it.'''

    output_log.clear() # clear the output log

    movie = random.choice(movies_list)
    print(movie,'\n')

    output_log.append(movie) # save the displayed result to the output_log

def begins_with():
    '''Prompt for a string and then search for and display all movies that start with this string.'''

    match = False # Set condition for printing the null result message

    output_log.clear() # clear the output log

    search = input('Find movies that begin with: ')

    print() # add a clear line before displaying results

    if not search: # return to menu if search string is empty
        return

    for movie in movies_list:

        if search.upper() == movie[0:len(search)].upper(): # check that the movie begins with the search string
            print(movie, '\n') # display the result
            output_log.append(movie) # save the displayed results to the output_log
            match = True # The null result message will not be printed if a match is found

    if not match: # null result message
        print('There are no movies that begin with "{}"'.format(search),'\n')

def find():
    '''Prompt for two search strings, then find and display all movies that contain the strings.
       If only the first string is provided, then find and display all movies that contain that string.'''

    match = False # Set condition for printing the null result message

    output_log.clear() # clear the output log

    print('Find movies that contain the following two strings,')

    searchOne = input('Search String One: ')

    if not searchOne: # return to menu if searchOne string is empty
        return

    searchTwo = input('Search String Two: ')

    print() # add a clear line before displaying results

    for movie in movies_list:

        if searchTwo == '': # if the second search string is blank, only check for a match against the first search string
            if searchOne.upper() in movie.upper(): # check that the movie contains the search string
                print(movie, '\n') # display the result
                output_log.append(movie) # save the displayed results to the output_log
                match = True # The null result message will not be printed if a match is found

        elif searchOne != '' and searchTwo != '': # check that there is a string in both search inputs
            if searchOne.upper() in movie.upper() and searchTwo.upper() in movie.upper(): #check that both search strings are in a movie
                print(movie, '\n') # display the result
                output_log.append(movie) # save the displayed results to the output_log
                match = True # The null result message will not be printed if a match is found

    if searchOne and not searchTwo: # condition for null result message where only searchOne was provided
        if not match: # null result message
            print('There are no movies that contain "{}"'.format(searchOne),'\n')

    if searchOne and searchTwo: # condition for null result message where searchOne and searchTwo were provided
        if not match: # null result message
            print('There are no movies that contain both of "{}" and "{}"'.format(searchOne, searchTwo),'\n')

def save():
    '''Save the last displayed movies to a list of favourites.'''

    if output_log: # check that there are movies to save
        for movie in output_log:

            if movie not in my_favourites_list: # only add movies that aren't already in the favourites list
                my_favourites_list.append(movie)
                print('saved {} to favourites'.format(movie),'\n')

            elif movie in my_favourites_list:
                print('{} is already saved to favourites'.format(movie),'\n')

    else:
        print('There are no display results to be saved','\n')

def my_favourites():
    '''Display the current favourites list.'''

    if my_favourites_list: # check that there are movies saved to the list
        print('Favourites: ',my_favourites_list,'\n')

    else:
        print("There are no movies in your favourites list",'\n')

while True:
    cmd = get_menu_option() # this function displays the menu and returns with a valid option
    if cmd == 'r':
        random_movie()
    elif cmd == 'b':
        begins_with()
    elif cmd == 'f':
        find()
    elif cmd == 's':
        save()
    elif cmd == 'm':
        my_favourites()
    elif cmd == 'c':
        my_favourites_list.clear()
        print('Your favourites list has been cleared','\n')
    elif cmd == 'q':
        print('Quitting program...')
        break
