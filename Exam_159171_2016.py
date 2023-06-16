# Exam 2016
# Question 1a

# for testing:
# print('12'*3)
# print("Good Morning".split())
# print(len([1,'+',2,'+',3]))

# answer:
# 121212
# ['Good', 'Morning']
# 5

# Question 1b

# for testing:
# G = 2
# d1 = 1
# d2 = 4
# r = 2
# answer:
# f = G*(((d1*d2)**3)/(r**2))

# for testing:
# print(f)

# Question 1c

# for testing:
# data = ['Sir','Bloggs',67]

# answer:

# print("{} {} is ({} inches) is {:.1f}m tall.".format(data[0], data[1],data[2], 67/39.371))

# Question 1d

# for testing
# s = '4'
# n = 4
#
# print(s*int(s))
# print(int(s)*3)
# print(str(n)*3)

# answer:

#4444
#12
#444

# Question 2a

# answer:

# for i in range(15,-1,-5):
#     print(i)

# Question 2b

# for testing:

# L = ['Alphabet', 'car']

# answer:

# count = 0
# while count < len(L):
#     if 'A' in L[count]:
#         print('{} contains an A'.format(L[count]))
#     else:
#         print('{} does not contain an A'.format(L[count]))
#     count += 1

# Question 2c

# for testing:

# L = [ "29.3", "tea", "1", None, 3.14 ]

# answer:

# D = []
# for item in L:
#     try:
#         D.append(float(item))
#     except:
#         D.append(item)

# for testing:

# print(D)

# Question 2d

# for testing:

# for i in range(1,3):
#     for j in ('hot','soup'):
#         print(i, j*i)

# answer:

# 1 hot
# 1 soup
# 2 hothot
# 2 soupsoup

# Question 3a

# for testing:
# hasInternet = False
# busStopDistance = 500
# distanceToShops = 500
# libraryWifiAccess = True
# rent = 'high'

# answer:
# if hasInternet and busStopDistance < 500 and distanceToShops < 500:
#     apply = 'yes'
# elif distanceToShops >= 500 and (hasInternet or libraryWifiAccess) and (rent == 'low' or rent == 'medium'):
#     apply = 'maybe'
# elif rent == 'high' and not hasInternet and busStopDistance >= 500 and distanceToShops >= 500:
#     apply = 'no'
# else:
#     apply = "don't know"

# for testing:
# print(apply)


# Question 3b

# for testing:

# def multiply(number):
#     p = number * 2
#     return p

# return a number or for some values, double the number
# def testNumber(number):
#     result = number
#     if (number >= 7 and number < 20):
#         result = multiply(number)
#         return result

# first_result = testNumber(5)
# print(first_result)
#
# second_result = testNumber(10)
# print(second_result)
#
# answer:
# def testNumber(number):
#     result = number
#     if (number >= 7 and number < 20):
#         result = multiply(number)
#         return result
#     else:
#         return result

# The error occurs when a number less than 7 is given as the argument
# to testNumber, as is the case for the statement: print(first_result).

# The error occurs because testNumber() does not have an else statement to handle parameters that
# are not caught by the if statement. To fix this error, add an else statement with 'return result', as
# shown above, so that the testNumber() function operates as specified by the comment above it.

# Question 4a

# for testing
# msg = 'What is your name?'
# msg2 = 'What are your favourite colors?'
# typeOfResult1 = 'getString'
# typeOfResult2 = 'getList'

# answer:

# def getResponses(msg,typeOfResult):
#     if typeOfResult == 'getString':
#         print(msg)
#         return input("reply: ")
#     elif typeOfResult == 'getList':
#         print(msg)
#         listOfReplies = []
#         while True:
#             reply = input('reply: ')
#             if reply == 'quit':
#                 return listOfReplies
#             else:
#                 listOfReplies.append(reply)

# for testing
# print("returned name was {}".format(getResponses(msg,typeOfResult1)))
# print("returned list was {}".format(getResponses(msg2,typeOfResult2)))

# Question 4b

# for testing:
# with open('spellCheck.txt','w') as spellCheck:
#     spellCheck.write('teh,the \n')
#     spellCheck.write('virrus,virus')

# answer:

# def checkSpelling(word, commonMistakes=False):
#     if commonMistakes == False:
#         return word
#     with open(commonMistakes,'r') as file:
#         for line in file:
#             if word == line.strip().split(',')[0]:
#                 return line.strip().split(',')[1]
#     return word

# for testing:
# word = 'teh'
# word1 = 'virrus'
# word2 = 'lava'
# word3 = 'the'
# commonMistakes = 'spellCheck.txt'
# print(checkSpelling(word,commonMistakes))
# print(checkSpelling(word1,commonMistakes))
# print(checkSpelling(word))
# print(checkSpelling(word2,commonMistakes))
# print(checkSpelling(word3,commonMistakes))

# Question 4c

# for testing:
# animal = 'cat'
# color = 'blue'
# clothing = 'shoe'
# car = 'skyline'
# A = [animal, color, clothing]
# B = [color, clothing, car]

# for testing:
# A = [1,2,3,4,5]
# B = [3,4,5,6,7]

# answer:
# Aonly = []
# Bonly = []
# Both = []
# for item in A:
#     if item in B:
#         Both.append(item)
#     else:
#         Aonly.append(item)
# for item in B:
#     if item not in A:
#         Bonly.append(item)

# for testing:

# print(Aonly)
# print(Bonly)
# print(Both)

# Question 5a

# answer:

# def wordListBuilder(wordList):
#     sentence = input("Enter a word or sentence: ")
#     for word in sentence.split():
#         if word.lower() not in [x.lower() for x in wordList]:
#             wordList.append(word)
#     return wordList

# for testing:
# input 'CAT is good'
# wordList = 'the cat jumped'.split()
# print(wordListBuilder(wordList))
# print(wordList)

# Question 5b

# answer:

# while True:
#     theList = wordListBuilder(wordList)
#     if len(theList) >= 10:
#         print(sorted(theList))
#         break

# Question 5c

# for testing:
# with open('numbers.txt','w') as numbers:
#     numbers.write("# Only add lines when first value is larger\n")
#     numbers.write("1 7\n")
#     numbers.write("20 1\n")
#     numbers.write("5 10\n")
#     numbers.write("40 2\n")

# answer:

# linesOfNumbers = 0
# selectedLines = 0
# runningTotal = 0
# with open('numbers.txt','r') as numbers:
#     for line in numbers:
#         if line.split()[0][0] != '#':
#             linesOfNumbers += 1
#             if int(line.strip().split()[0]) > int(line.strip().split()[1]):
#                 selectedLines += 1
#                 runningTotal += int(line.strip().split()[0]) + int(line.strip().split()[1])
# print("There were {} lines of numbers".format(linesOfNumbers))
# print("The sum of the {} selected lines is {}".format(selectedLines,runningTotal))

# Question 6a


# for testing:
# MP3List = [['kanye west', 'dark fantasy', 'monster'],['black eyed peas','the e.n.d.','just cant get enough']]

# answer:
# def find_track(s):
#     for l in MP3List:
        # if s in l[2]:
            # print('''Artist: {}, Album: {}, Track: {}'''.format(l[0],l[1],l[2]))

# for testing:

# find_track('st')

# Question 6b

# Searching through a list involves a linear search of the list indices until a matching value is found,
# therefore the time it takes to find a match is proportional to the number of items in the list
# (this can also be expressed as O(n) time complexity. For instance, to find 'cat' in the list,
# ['dog','sheep','cat','wolf'], a linear search of the list indices will be performed until a match for 'cat' is found.
#
# Dictionaries can achieve faster lookup times because they use a hash function to generate a hash table
# index based on the key of the key-value pair that will be stored in the hash table. So long as a good hash
# function is used, there will be few collisions, so a key can usually be found directly by looking up the index
# associated with its hash value, rather than need to look up every index in a linear fashion.
# This makes dictionaries typically much faster than lists when looking up keys in a dictionary compared to looking up values in a list.
# For instance, to find the key 'cat' in the dictionary {'dog': 1, 'sheep': 1, 'cat': 1, 'wolf': 1},
# the hash of 'cat' will provide the index of it's location in the dictionary. ' \
# 'This can also be expressed as O(1) time complexity, meaning the dictionary typically does not have slower look up times as the dictionary gets larger.
#
# Lists are ordered, whereas the dictionary hash process means that dictionaries are not ordered. This makes lists more useful
# for operations that require preservation of order, for instance, with a list of movies watched (['the matrix'],['kill bill']),
# the 'last movie watched' could immediately be accessed by index or with list.pop(), whereas a dictionary of movies watched would require additional
# information to be stored with every movie in order to know which one was watched most recently.
