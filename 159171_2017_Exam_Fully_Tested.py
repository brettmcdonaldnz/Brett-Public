# Answers and Learnings from 159.171 Exam 2017.
# I've tested all of the answers, and they would achieve full marks as far as I can tell.

# Question 1a
# Learnings: int() doesn't apply rounding to the decimal point, it just trims it off.
# answer:
# 1234
# ['NICE D','Y']
# 40
# False
# >>3.142<<
# for testing:
# print(int(1234.56))
# print("Nice Day".upper().split('A'))
# print(len('55.3')*10)
# print(15 % 2 == 0)
# print(">>%0.3f<<" % (3.1415926))

# Question 1b
# for testing:
# x = 2
# answer:
# y =  ((3*x**3) - (5*x**2) + (7*x) + 9)**0.5
# for testing:
# print(y) # should be about 5

# Question 1c
# for testing:
# title = ['roof', 'walls', 'doors']
# colors = ['green', 'blue', 'red']
# answer:
# for i in range(len(colors)):
#     print('{} {}'.format(colors[i], title[i]))
# for testing: it should display green roof, blue walls, red doors on separate lines.

# Question 1d
# answer:
#'None' is printed because def volume() does not have a return statement. To fix the error, within def volume(), replace print() with return.
# for testing:
# import math
# def volume(radius, length):
#     return int(math.pi * radius**2 * length)
# print("Volume =", volume(2,10)) # should display 'Volume = 125'

# Question 2a
# Learnings: Make sure not say 'else' when you mean 'except' in a try/except block.
# answer:
# def update(L, word, word2):
#     try:
#         L[L.index(word)] = word2
#         return L, True
#     except:
#         return L, False
# for testing:
# print(update(['hello', 'hi', 'welcome', 'bye'] , 'welcome', 'goodbye'))
# it should display ['hello', 'hi', 'goodbye', 'bye'] and True

# Question 2b
# answer:
# red
# redredred
# green
# greengreengreen
# blue
# blueblueblue
# for testing:
# for colour in ['red', 'green', 'blue']:
#     for value in range(1,5,2):
#         print(value*colour)

# Question 2c
# for testing:
# L = ['It is', 'time', 'for', 'tea']
# answer:
# K = []
# for item in L:
#     subList = []
#     subList.append(len(item))
#     subList.append(item)
#     K.append(subList)
# for testing:
# print(K) # it should be [[5,'It is'], [4,'time'],[3,'for],[3,'tea']]

# Question 2d
# answer:
# count = 1
# while count < 31:
#     if count % 5 != 0 and count % 7 != 0:
#         print(count)
#     count += 1
# for testing: It shouldn't display multiples of 5 or 7.

# Question 3a
# Learnings: make sure to use == for comparison, and not =.
# for testing
# location = 'outside'
# weather = 'sunny'
# time = 1200
# wind_speed = 50
# answer:
# l = location
# w = weather
# t = time
# wind = wind_speed
# use_umbrella = False
# need_sunglasses = False
# if l == 'outside' and (w == 'rainy' or w == 'stormy') and wind < 30:
#     use_umbrella = True
# if l == 'outside' and 1000 <= t <= 1600 and w == 'sunny':
#     need_sunglasses = True
# for testing:
# print(use_umbrella) # should be False
# print(need_sunglasses) # should be True

# Question 3b
# answer:
# 25 blue
# for testing:
# def f2(x, y):
#     if not x > y:
#         return 'Red'
#     else:
#        return 'Blue'
# def Test(x):
#     if x < 0:
#         p = f2(2,4)
#     else:
#         p = f2(4,2)
#     print(x**2,p)
# Test(5)

# Question 4a
# Learnings: the line.lstrip()[0] operation will cause an 'index out of range' error on empty lines. Therefore, always use a try/except block when checking for empty lines and '#' ad the same time.
# for testing:
# with open('input.py','w') as input:
#     input.write("# This is a file of categories\nAnimals: cat, dog, frog, cheetah, tiger\nItems: desk, chair, bus cups, pencil\n\nTechnology: cellphone, TV, laptop, wifi-router\n\t\t# That's end of the file")
# answer:
# with open('input.py','r') as input, open('output.py','w') as output:
#     for line in input:
#         try:
#             if line.lstrip()[0] != '#' and line != '\n':
#                 output.write(line)
#         except:
#             pass
# for testing:  The output should be lines 1, 4 and 6 (start with Animals, Items and Technology)

# Question 4b1
# Learnings: always double-check bracket balancing, especially brackets are nested several times.
# answer:
# def lookup(int_num):
#     int_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#     return int_dict[int_num]
# for testing:
# print(lookup(4)) # it should display 'four'
# Question 4b2
# answer:
# int_list = [1,2,3,4,5]
# remove_num = int(input('Omit which number? '))
# int_list.pop(int_list.index(remove_num))
# for i in int_list:
#     print('{} --> {}'.format(i,lookup(i)))
# for testing: It should show everything except 4 if 4 is given as the argument.

# Question 4c
# Learnings: Pay close attention to variable name capitalisation (I only found error 2 through testing)
# answer:
# 1. 'n' is not defined on line 3; the range(n) function  will fail.
# 2. 'Question' is not defined in the function, this will cause it fail. (the function uses 'question' - with a lowercase 'q' as the parameter).
# 3. reply does not have .lower() on line 5; case-independency will not be applied
# 4. reply == valid_answers.lower() will fail the equality check on line 5; they are comparing a string to a list rather than a string to a string.
# 5. .lower() can't be applied to the list valid_answers on line 5; the .lower() function will fail.
# 6. There is no parameter after return on line 6, the function will return None instead of a valid answer.
# 7. return reply on line 9 can't be reached because it outside of the if/else block.
# 8. A question mark is added to the question parameter on line 11; this will add unnecessary duplication of the question mark when input(Question + '? ') is called on line 5.
# for testing:
# def getReply(question, valid_answers):
    #               question is a string, valid_answers is a list
    # for x in range(n):
    #     reply = input(Question + '? ')
    #     if reply == valid_answers.lower():
    #         return
    #     else:
    #        return False
    #     return reply

# print(option = getReply('Show next option? ', ['yes','no','y','n']))

# Question 5a
# Learnings: make sure to put a ':' after declaring a function.
# answer:
# def build_dict():
#     dict = {}
#     while True:
#         key = input('key  : ')
#         if key == 'quit':
#             return dict
#         try:
#             key = float(key)
#         except:
#             pass
#         value = input('value: ')
#         if key not in dict:
#             dict[key] = [value]
#         else:
#             if value in dict[key]:
#                 print('>> duplicate - ignored')
#             else:
#                 dict[key].append(value)
# for testing:
# print(build_dict()) #args color, red, 3.5, 68, color, blue, color, red, quit should display { 'color': ['red', 'blue'], 3.5: ['68']}

# Question 5c
# Learnings: when doing calculations (in this case, adding credit values), always make sure you have an int() or float() as appropriate.
# answer:
# entries = 0
# credit = 0
# with open('data.txt','r') as f:
#     for line in f:
#         if line.lstrip()[0] != '#':
#             entries += 1
#             try:
#                 credit += float(line.split(',')[1])
#             except:
#                 pass
# print('There were {} Entries'.format(entries)) # should be There were 3 Entries
# print('The total credit is ${:.2f}'.format(credit)) # should be The total credit is $584.39

# Question 6a
# Learnings: it is easy to get = and == mixed up, especially when using them alternatingly. With every use, think carefully if you are comparing (==), or assigning(=).
# for testing:
# s = 'It was freezing outside but the cake in the oven would help'
# answer:
# words_in_string = len(s.split()) # should be 12
# longest = 0
# all_longest = [] # should be 'freezing'
# shortest = 1000
# all_shortest = [] # should be ['it', 'in]
# words_with_o = 0 # should be 3
# total_ch_excl_sp = 0 # should be 48
# for word in s.split():
#     if len(word) > longest:
#         longest = len(word)
#         all_longest = [word]
#     elif len(word) == longest:
#         all_longest.append(word)
#     if len(word) < shortest:
#         shortest = len(word)
#         all_shortest = [word]
#     elif len(word) == shortest:
#         all_shortest.append(word)
#     if 'o' in word:
#         words_with_o += 1
#     total_ch_excl_sp += len(word)
# for testing:
# print(words_in_string,all_longest,all_shortest,words_with_o,total_ch_excl_sp)

# Question 6b
# answer:
# list lookup times can be much slower than dictionary lookup times because lists are searched by index in a linear fashion,
# meaning indices are evaluated iteratively until a match for the lookup term is found.
# This means the lookup time is proportional to the length of the list, if the index is not known.
# This can be expressed as O(n) time complexity.
#
# Conversely, dictionaries achieve an almost constant lookup time because they use the hash of a key in a key value pair
# to generate the index where the key value pair will be stored in a hash table. Therefore, to retrieve the key value pair
# from the hash table, the index can be found by running the hash function on the key, and so the key value pair can be found immediately,
# so long as a good hash function is used so that there are few collisions. Thus, when searching by key, dictionaries have an almost
# constant look up time, which can also be expressed as O(1) time complexity.
#
# However, lists have a feature that makes them more useful for some tasks: lists are ordered, whereas dictionaries are not ordered.
# So for instance, it is faster to retrieve the most recently watched movie from a list (because it will be the last item in a list,
# so the index is known) than from a dictionary. To retrieve it from a dictionary, the dictionary would need the 'most recently watched'
# status as a tag or a timestamp in the values associated with the movie keys, so every key in the dictionary will need to be evaluated
# to determine which one was the most recently watched movie - this could be significantly slower than just accessing the last index in a list.




