# By Brett McDonald
# SID: 10158931
# Assignment 2A
# Question 3

stories = [
  ['With bloody hands, I say good-bye.'                    , 'Frank Miller'],
  ['TIME MACHINE REACHES FUTURE!!! ... nobody there ...'   , 'Harry Harrison'  ],
  ['The baby\'s blood type? Human, mostly.'                , 'Orson Scott Card'],
  ['For sale: baby shoes, never worn.'                     , 'Ernest Hemingway'],
  ['Corpse parts missing. Doctor buys yacht.'              , 'Margaret Atwood'],
  ['We kissed. She melted. Mop please!'                    , 'James Patrick Kelly'],
  ['Starlet sex scandal. Giant squid involved.'            , 'Margaret Atwood'],
  ['Will this do (lazy writer asked)?'                     , 'Ken McLeod'     ],
  ["I'm sorry, but there's not enough air in here for everyone. I’ll tell them you were a hero.",   'J. Matthew Zoss'],
  ['Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head','Mike Jackson'],
  ["Not In My Job Description: Make sure it's done by the end of the day Jones.\nBut, sir, it's not in my ....\nJust do it, and remember, no blood."             ,'Mike Jackson'],
  ['Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?'             ,'Mike Jackson'],
  ['Forgot My Own Name: The hospital said it was concussion.\nMight be permanent memory loss.\nCan\'t even remember my own name - which is handy considering who I am.','Mike Jackson']
]

def get_menu_option():
    '''displays a menu and carries out the appropriate action depending on
        which letter the user types, and then re-displays the menu'''

    print('*** Story Explorer ***')
    print('   w - find stories that contain a certain word (e.g. sky)')
    print('   a - find stories by a certain author')
    print('   x - find stories by a certain author and containing a certain word')
    print('   n - find stories less than a certain number of words')
    print('   d - display all stories')
    print('   q - quit')
    command = input('command: ?')
    print()

    return command.lower()

def by_word():
    '''Display all stories that contain a certain word in the story as a string or substring (not including the author)'''

    match = False # Set condition for printing the null result message

    word = input('Enter a word: ')

    print() # add a clear line before displaying results

    if not word: # Return to the menu if no word is provided
        return

    for story in stories:

        if word.upper() in story[0].upper(): # check that the word is in the story
            print('"{}"\n\t-- {}'.format(story[0],story[1]),'\n') # format output with author below the story
            match = True # The null result message will not be printed if a match is found

    if not match: # null result message
        print('There are no stories that contain the word "{}"'.format(word),'\n')

def by_author():
    '''Display all stories that contain a given string as a string or substring in the author of a story'''

    match = False # Set condition for printing the null result message

    author = input('Enter an author: ')

    if not author: # Return to the menu if no author is provided
        return

    print() # add a clear line before displaying results

    for story in stories:
        if author.upper() in story[1].upper(): # check that the author is in the author part of the story
            print('"{}"\n\t-- {}'.format(story[0],story[1]),'\n') # format output with author below the story
            match = True # The null result message will not be printed if a match is found

    if not match: # null result message
        print('There are no stories with authors that contain "{}"'.format(author),'\n')

def by_author_and_word():
    '''Display all stories by a certain author and containing a certain word.
        Return to the menu if the user does not provide an author and a word string.'''

    match = False # Set condition for printing the null result message

    author = input('Enter an author: ')

    if not author: # Return to the menu if no author is provided
        return

    word = input('Enter a word: ')

    if not word: # Return to the menu if no word is provided
        return

    print() # add a clear line before displaying results

    for story in stories:
        if author.upper() in story[1].upper() and word.upper() in story[0].upper(): # check that both conditions are met
            print('"{}"\n\t-- {}'.format(story[0],story[1]),'\n') # format output with author below the story
            match = True # The null result message will not be printed if a match is found

    if not match: # null result message
        print('There are no stories that meet both of the conditions: author contains "{}" and story contains "{}"'.format(author,word),'\n')

def max_words():
    '''Find stories with less than a certain number of words'''

    match = False # Set condition for printing the null result message

    word_max = input('Enter a maximum number of words: ')

    if not word_max: # Return to the menu if no maximum word count is provided
        return

    print() # add a clear line before displaying results

    for i in word_max:
        if i not in '1234567890':
            print('"{}" is not a valid integer'.format(word_max),'\n')
            return

    for story in stories:
        if len(story[0].split()) < int(word_max):
            print('"{}"\n\t-- {}'.format(story[0],story[1]),'\n') # format output with author below the story
            match = True # The null result message will not be printed if a match is found

    if not match: # null result message
        print('There are no stories that have less than {} words'.format(word_max),'\n')

def display_all():
    '''Display all stories'''
    for story in stories:
        print('"{}"\n\t-- {}'.format(story[0],story[1]),'\n') # format output with author below the story

while True:
    cmd = get_menu_option() # this function displays the menu and returns with a valid option
    if cmd == 'w':
        by_word()
    elif cmd == 'a':
        by_author()
    elif cmd == 'x':
        by_author_and_word()
    elif cmd == 'n':
        max_words()
    elif cmd == 'd':
        display_all()
    elif cmd == 'q':
        print('Quitting program...')
        break
