# Exam 2017
# Question 1a

# for testing:
# print(int(1234.56))
# print("Nice Day".upper().split('A'))
# print(len('55.3')*10)
# print(15 % 2 == 0)
# print(">>%0.3f<<" % (3.1415926))

# answer:
# 1234
# ['NICE D', 'Y']
# 40
# False
# >>3.142<<

# Question 1b

# for testing:
# x = 1

# answer:
# y = ((3*x**3)-(5*x**2)+7*x+9)**0.5

# for testing:
# print(y)

# Question 1c

# answer:
# title = ['roof','walls','doors']
# colors = ['green','blue','red']
# for i in range(len(title)):
#   print("{} {}".format(colors[i],title[i]))

# Question 1d

# for testing:
# import math
# def volume(radius, length) : # calculate the volume of a cylinder
#   print(int(math.pi * radius**2 * length))

# print("Volume =", volume(2,10))

# def volume2(radius, length) : # calculate the volume of a cylinder
#   return int(math.pi * radius**2 * length)

# print("Volume =", volume2(2,10))

# answer
# volume() has a print() argument inside of it, but it does not have a return argument.
# So, when volume(2,10) is called by print(), it will run its internal print() argument, which
# evaluates to 125, but volume(2,10) returns 'None', so print("volume =", volume(2,10))
# will display 125 on a line, then Volume = None on the next line.

# To fix the error, inside volume(), replace print() with return.

# Question 2a

#answer:

# def update(L,word,word2):
#   success = False
#   for i in L:
#     if i == word:
#       L[L.index(i)] = word2
#       success = True
#       break
#   return L, success

# testing:

# print(update(["hello","hi","welcome","bye"] , "welcome", "goodbye"))

# Question 2b

# testing:
# for colour in ['red','green','blue']:
#   for value in range(1, 5, 2):
#     print(value*colour)

# answer:
# red
# redredred
# green
# greengreengreen
# blue
# blueblueblue

# Question 2c

# for testing:
# L = [ 'it is', 'time', 'for', 'tea']

# answer:
# K = []
# for i in L:
#   subK = []
#   subK.append(len(i))
#   subK.append(i)
#   K.append(subK)

# for testing:
# print(K)

# Question 2d

#answer:
# count = 0
# while count < 30:
#   count += 1
#   if count % 5 != 0 and count % 7 != 0:
#     print(count)

# print(int(1234.56))

# Question 3a

# for testing

# location = 'outside'
# weather = 'sunny'
# time = 1200
# wind_speed = 25

#answer:
# use_umbrella = False
# need_sunglasses = False
# if location == 'outside' and (weather == 'rainy' or weather == 'stormy') and wind_speed < 30:
#     use_umbrella = True
# if location == 'outside' and 1000 <= time <= 1400 and weather == 'sunny':
#     need_sunglasses = True

# for testing:
# print(use_umbrella)
# print(need_sunglasses)

# Question 3b

# for testing

# def f2(x, y):
#     if not x > y:
#         return 'Red'
#     else:
#         return 'Blue'
#
# def Test(x):
#     if x < 0:
#         p = f2(2,4)
#     else:
#         p = f2(4,2)
#
#     print(x**2, p)
#
# Test(5)

# answer:
# 25 Blue

# Question 4a

# answer:
# with open('input.py','r') as input, open('output.py','w') as output:
#     output.writelines([line for line in input if line != '\n' and line.lstrip()[0] != '#'])


# Question 4b1

# answer:
# def lookup(int_num):
#     pairs = [[1,'one'],[2,'two'],[3,'three'],[4,'four'],[5,'five']]
#     for i in range(len(pairs)):
#         if pairs[i][0] == int_num:
#             return pairs[i][1]

# Question 4b2

# answer:
# def print_num():
#     omit = int(input('Omit which number? '))
#     for i in range (1,6):
#         if i == omit:
#             continue
#         else:
#             print('{} --> {}'.format(i,lookup(i)))

# print_num()

# Question 4c

# for testing:
# def getReply(question, valid_answers):
#     while True:
#         reply = input(question + '?')
#         if reply.lower() in valid_answers:
#             return reply.lower()
#
# print(getReply('Show next option? ', ['yes', 'no', 'y', 'n']))

# answer:
# for x in range(n): # x and n are not defined, this should be 'while True:'
#     if reply == valid_answers.lower() # reply should be 'reply.lower()', # .lower() can't be used on a list
#         return # nested returns will prevent 'return reply' from being accessed
#     else: # 'else': is not required in this function if it is in a while loop
#         return False # this statement is redundant and will prevent 'return reply' from being accessed
# return reply         # return reply should be return reply.lower()
# in 'Show next option? ', the '?' is redundant because input() appends '?' to the question string

# Question 5a

# answer:
# def dict_build():
#     dict = {}
#     while True:
#         key = input("key: ")
#         if key == 'quit':
#             return dict
#         try:
#             key = float(key)
#         except:
#             key = key
#         value = input("value:")
#         if dict.get(key):
#             if value in dict[key]:
#                 print(">> duplicate - ignored")
#             else:
#                 dict[key].append(value)
#         else:
#             dict[key] = [value]
#
# # for testing:
# print(dict_build())

# Question 5b

# for testing:
# fileWrite = open('data.txt','w')
# fileWrite.write("#Name,   Credit,   Contact\n")
# fileWrite.write('Felicity,373.25,Felicity@hotmail.com\n')
# fileWrite.write('Arthur,xxx,Art@gmail.com\n')
# fileWrite.write('William,211.14,@Billl\n')
# fileWrite.close()
#
# # answer:
#
# credit = 0
# entries = 0
# with open('data.txt','r') as data:
#     for line in data:
#         if line.split()[0][0]!= '#':
#             entries += 1
#             try:
#                 credit  += float(line.split(',')[1])
#             except:
#                 continue
# print("There were {} Entries".format(entries))
# print("The total credit is ${:.2f}".format(credit))

# Question 6a

# for testing:
# s = "It was freezing outside but the cake in the oven would help"

# answer:
# num_words = len(s.split())
# longest = 0
# longest_words = []
# shortest = 1000
# shortest_words = []
# num_words_with_o = 0
# total_char_excl_spaces = 0
# for word in s.split():
#     if len(word) > longest:
#         longest = len(word)
#         longest_words = [word]
#     elif len(word) == longest:
#         longest_words.append(word)
#     if len(word) < shortest:
#         shortest = len(word)
#         shortest_words = [word]
#     elif len(word) == shortest:
#         shortest_words.append(word)
#     if 'o' in word.lower():
#         num_words_with_o += 1
#     total_char_excl_spaces += len(word)

# for testing:
# print(num_words)
# print(longest_words)
# print(shortest_words)
# print(num_words_with_o)
# print(total_char_excl_spaces)

# Question 6b

# answer:
# Searching for items in a list is a linear search, this means that the list indices are checked
# one at a time for a matching item, therefore the time it takes to find an item in a list is proportional
# to the number of items in a list. This property of list lookup times can be expressed as
# O(n) time complexity.

# Conversely, dictionaries have an almost constant lookup time (O(1) time complexity) regardless of
# the number of items in the dictionary, so long as the dictionary implements a good hash function,
# which makes collisions uncommon.

# Dictionaries achieve O(1) lookup times by using the item key as the key for a hash function,
# which generates an algorithmically random index that is stored in a hash table, along
# with the values associated with that item key. Therefore, when looking up a key in a dictionary,
# the hash of the key will provide its index, and the values for that key can be retrieved directly from
# the hash table without having to search the hash table linearly.

# Lists are ordered, and dictionaries are not ordered. This gives lists an advantage for operations that
# require order, such as preserving order when inserting or deleting values, sorting values into a
# sequential index, or iterating over values by sequential index.

# def countWords(thisWord,listOfWords):
#     return sum(1 for word in listOfWords if word == thisWord)
#
# targetWords = ['cat','horse']
# listOfWords = ['cat','cat','dog']
#
# def countWordS(targetWords,listofWords):
#     for word in targetWords:
#         print('''"{}" occurs {} times.'''.format(word,countWords(word,listofWords)))
#
# countWordS(targetWords,listOfWords)

