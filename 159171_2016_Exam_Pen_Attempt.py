# Answers and Learnings from 159.171 Exam 2016.
# I've tested all of the answers, and they would achieve full marks as far as I can tell.

# Question 1a
# answer
# 121212
# ['Good', 'Morning']
# 5
# for testing:
# print("12"*3)
# print("Good Morning".split())
# print(len([1,'+',2,'+',3]))

# Question 1b
# for testing:
# G = 10
# d1 = 2
# d2 = 4
# r = 3
# answer:
# f = G*((d1*d2)**3 / r**2)
# for testing:
# print(f) # f should be about 500

# Question 1c
# for testing:
# data = ["Sir", 'Bloggs', 67]
# answer:
# print('{} {} is ({} inches) is {:.1f}m tall.'.format(data[0],data[1],data[2],data[2] / 39.371))
# for testing: code above should display 'Sir Bloggs is (67 inches) is 1.7m tall.'

# Question 1d
# answer:
# 4444
# 12
# 444
# for testing:
# s = "4"
# n = 4
# print(s*int(s))
# print(int(s)*3)
# print(str(n)*3)

# Question 2a
# answer:
# for i in range(15,-1,-5):
#     print(i)
# for testing: should display the following:
# 15
# 10
# 5
# 0

# Question 2b
# for testing:
# L = [ "Alphabet", "car"]
# answer:
# count = 0
# while count < len(L):
#     if 'A' in L[count]:
#         print('{} contains an A'.format(L[count]))
#     else:
#         print('{} does not contain an A'.format(L[count]))
#     count += 1
# for testing: # should display the following:
# Alphabet contains an A
# car does not contain an A

# Question 2c
# for testing:
# L = ["29.3", "tea", "1", None, 3.14]
# answer:
# D = []
# for item in L:
#     try:
#         if '.' in item:
#             D.append(float(item))
#         else:
#             D.append(int(item))
#     except:
#         D.append(item)
# print(D) # should display: [ 29.3, "tea", 1, None, 3.14]

# Question 2d
# answer:
#1 hot
#1 soup
#2 hothot
#2 soupsoup
# for testing:
# for i in range(1,3):
#     for j in ['hot', 'soup']:
#         print(i, j*i)

# Question 3a
# for testing:
# distanceToShops = 600
# hasInternet = False
# busStopDistance = 600
# libraryWifiAccess = False
# rent = 'high'
# answer:
# d = distanceToShops
# h = hasInternet
# b = busStopDistance
# l = libraryWifiAccess
# r = rent
# if h and b < 500 and d < 500:
#     apply = 'yes'
# elif d >= 500 and (h or l) and (r == 'low' or r == 'medium'):
#     apply = 'maybe'
# elif r == 'high' and not h and not l and not b < 500 and not d < 500:
#     apply = 'no'
# else:
#     apply = "don't know"
# for testing:
# print(apply) # should display 'no'

# Question 3b
# answer:
# the print statement - print(first_result) will not display a number, it will display 'None'.
# This is because the testNumber function has its 'return result' statement as part of the if statement,
# which only catches numbers between 7 (inclusive) and 20 (exclusive). To fix the error so that it behaves
# according to the comment, "return the number or for some values, double the number", the 'return result'
# statement needs to be moved one tab to the left.
# for testing:
# def multiply(number):
#     p = number * 2
#     return p
#
# def testNumber(number):
#     result = number
#     if(number >= 7 and number < 20):
#         result = multiply(number)
#         return result
#
# first_result = testNumber(5)
# print(first_result)
#
# second_result = testNumber(10)
# print(second_result)

# Question 4a
# answer:
# def getResponse(msg, typeOfResult):
#     if typeOfResult == 'getString':
#         return input(msg)
#     if typeOfResult == 'getList':
#         list = []
#         print(msg)
#         while True:
#             response = input('>> ')
#             if response == 'quit':
#                 return list
#             else:
#                 list.append(response)
# for testing:
# print(getResponse(msg='fav animal: ', typeOfResult='getString')) # should print 'cat'
# print(getResponse(msg='fav animals: ', typeOfResult='getList')) # should print ['cat','dog']

# Question 4b
# Learnings: when useing open(), make sure to give the 'r', or 'w' argument, and also to refer to the file by the variable (such as 'f')
#  after declaring that variable.
# answer:
# def checkSpelling(word, commonMistakes=False):
#     if not commonMistakes:
#         return word
#     else:
#         with open(commonMistakes,'r') as file:
#             for line in file:
#                 if word == line.split(',')[0]:
#                     return line.split(',')[1].strip()
#             return word
# for testing:
# with open('mistakes.txt','w') as f:
#     f.write('teh,the\nvirrus,virus')
# print(checkSpelling(word='teh',commonMistakes='mistakes.txt')) # should display 'the'
# print(checkSpelling(word='virrus',commonMistakes='mistakes.txt')) # should display 'virus'
# print(checkSpelling(word='viras',commonMistakes='mistakes.txt')) # should dispaly 'viras'
# print(checkSpelling(word='horse',commonMistakes='mistakes.txt')) # should return 'horse'
# print(checkSpelling(word='cat')) # should return 'cat'

# Question 4c
# for testing:
# A = ['cat','dog','shoe']
# B = ['dog','shoe','horse']
# answer:
# Aonly = []
# Bonly = []
# Both = []
# for item in A:
#     if item in B:
#        Both.append(item)
#     else:
#        Aonly.append(item)
# for item in B:
#     if item not in A:
#         Bonly.append(item)
# for testing:
# print(Aonly) # should print ['cat']
# print(Bonly) # should print ['horse']
# print(Both) # should print ['dog', 'shoe']

# Question 5a
# Learnings: be careful when generating a new list; use [:] to shallow copy the list if a new list needs to be returned that doesn't modify the original.
# Always make sure your builtin fuctions have (), as in .lower()
# answer:
# def build_sent(listOfWords):
#     newList = listOfWords[:]
#     response = input('enter word or sentence: ')
#     for word in response.split():
#         if word.lower() not in [x.lower() for x in newList]:
#             newList.append(word)
#     return newList
# for testing:
# print(build_sent(listOfWords=['cat','dog'])) # response as 'the Cat and Dogs' should display a new list as ['cat','dog','the','and','Dogs']

# Question 5b
# for testing:
# def build_sent(listOfWords):
#      newList = listOfWords[:]
#      response = input('enter word or sentence: ')
#      for word in response.split():
#          if word.lower not in [x.lower for x in newList]:
#              newList.append(word)
#      return newList
# answer:
# while True:
#     newList = build_sent(listOfWords=['cat','dog'])
#     if len(newList) >= 10:
#         print (sorted(newList))
#         break
# for testing: call the above function with varying sentence lengths, it should only break and print if the the new list is equal or greater than 10 words. I've interpreted the question as generating a new list with each function call, rather than adding the list with each function call (which would be recursive, which was not covered in 159.171)

# Question 5c
# for testing:
# with open('numbers.txt','w') as f:
#     f.write('# Only add lines when first value is larger\n1   7\n20    1\n5   10\n40   2')
# answer
# lines = 0
# selected_lines = 0
# sum = 0
# with open('numbers.txt','r') as f:
#     for line in f:
#         if line.lstrip()[0] != '#':
#             lines += 1
#             if int(line.split()[0].strip()) > int(line.split()[1].strip()):
#                 sum += int(line.split()[0].strip()) + int(line.split()[1].strip())
#                 selected_lines += 1
# print('There were {} lines of numbers'.format(lines))
# print('The sum of the {} selected lines is {}'.format(selected_lines,sum))
# for testing should display:
# There were 4 lines of numbers
# The sum of the 2 selected lines is 63

# Question 6a
# Learnings: don't over-think how to look through the index of a nested list. Just look through the index of each sublist as you iterate over the sublists.
# Be careful with {:>10}, make sure the ':' is included.
# There are two ways of going about this question (the exam is not clear on it); you could add the mp3list as a parameter to the function, or as I've done below,
# you could call 'global mp3List' within the function to refer to the mp3List mentioned by the question.
# answer:
# def find_tracks(track_string):
#     global mp3List
#     for entry in mp3List:
#         if track_string in entry[2]:
#             print('Artist: {:>10}, Album: {:>10}, Track: {:>10}'.format(entry[0],entry[1],entry[2]))
# for testing:
# mp3List = [['Louis Armstrong', 'Ella and Louis again', "don't be that Way"],['Louis Armstrong', 'Porgy and Bess', 'Summertime']]
# find_tracks(track_string='Summer') # should display one result
# find_tracks(track_string='t') # should display two results

# Question 6b
# answer:
# Lists usually have much slower lookup times than dictionaries because the lookup is a linear search;
# that means that each index is checked for a match until a match is found. Therefore list lookup times are proportional to
# the size of the list (this can also be expressed as O(n) time complexity. Conversely, dictionaries use a hash function based on
# the key to store the key value pair in a hash table, so a key value pair can be directly retrieved from its index in the hash table
# by running the hash function on the key (so long as it is a good hash function, and few collisions occur).
# This makes dictionaries typically much faster to lookup than than lists, because the index is usually already known based on the key,
# so the lookup times are not necessarily proportional to the size of the dictionary (this can also be expressed as O(1) time complexity).
#
# For example, lists or dictionaries could be used for storing a table of movies watched. If you wanted to know if the movie 'Kill Bill' had been watched,
# then in a list of movies (['Gran Turino', 'The Matrix', 'Kill Bill']) each index would need to be checked for a match.
# However, in a dictionary ({'Gran Turino': 'watched', 'The Matrix': 'watched', 'Kill Bill': 'watched'}), the movie 'Kill Bill'
# could be found immediately based on the hash of the key 'Kill Bill'. However, lists are ordered, whereas dictionaries are not ordered,
# which makes lists more useful for operations where order is desirable. For instance, to find the most recent movie watched,
# the movie can be directly accessed as the last index in the list. However, to know what the last movie watched was in a dictionary,
# the dictionary would need to add additional information about the time each movie was watched, and every index in the dictionary would need to be searched
# to determine which movie had the most recent viewing time stamp.


