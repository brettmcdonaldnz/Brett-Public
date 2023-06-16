# Answers and Learnings from 159.171 Exam 2015.
# I've tested all of the answers, and they would achieve full marks as far as I can tell.
# Question 1a
# answer:
#3737
#e
#77

# for testing:
# print ("37" + "37")
# print ("Hello"[1])
# print('37'.replace('3', '7'))

# Question 1b
# for testing:
# L = 2
# C = 4
# answer:
# import math

# f = 1 / ((2 * math.pi) * (L*C)**0.5)

# for testing:
# print(f)

# Question 1c
# for testing:
# PetrolGrade = 'Super'
# Amount = 25
# costPerLitre = 1.75

# answer:
# print('The cost of {} litres of {} is ${:.2f}'.format(Amount,PetrolGrade,Amount*costPerLitre))

# Question 1d
# answer:
#333
#9
#9
#333
# for testing:
# s = '3'
# n = 3
# print(s*3)
# print(n*3)
# print(int(s)*3)
# print(str(n)*3)

# Question 2a
# answer:
# list = []
# for i in range(1,26,3):
#     list.append(i)
# print(list)
# for testing:
# should display [1,4,7,10,13,16,19,22,25]

# Question 2b
# Learnings: This seems like a 'for i in range' question, but beware that floats can't be used as arguments in the range function. Therefore, use a while loop.
# Learnings: Note that all the numbers need to have one decimal place, so use {:.1f} to achieve this.
# Learnings: The easy way to check if a number is between two other numbers (with '=' if inclusive) is the following pattern: low <= number <= high
# answer:
# step = float(input('Stepsize   ?'))
# lower = int(input('Lower limit?'))
# upper = int(input('Upper limit?'))
# count = 1.5
# while count < upper+step:
#     if lower <= count <= upper:
#         print('{:.1f} BETWEEN'.format(count))
#     else:
#         print('{:.1f} Excluded'.format(count))
#     count += step

# Question 2c
# Learnings: Think carefully about index numbers. The string index starts at 0, so need to use count-1 to access the first letter, if count starts at 1.
# answer:
# count = 0
# string = 'Hello'
# while count < len(string):
#     print('{}: {}'.format(count+1,string[count]))
#     count += 1

# Question 2d
# Learnings: Pay close attention to end = " "; this will put a space between each output.
# Learnings: Think carefully about how print() works: it prints the output at the current location (might be on an existing line), and then adds a line break ('\n')
# answer:
#1
#2 2 2
#1
#2 2 2

# for testing:
# for numA in range(2):
#     print(1)
#     for numB in range(3):
#         print(2, end = " ")
#     print()

# Question 3a
# for testing:
# Temperature = 38
# hadFluShot = True
# PollenAllergy = True
# wateryEyes = True
# Season = 'Spring'
# answer:
# t = Temperature
# h = hadFluShot
# p = PollenAllergy
# w = wateryEyes
# s = Season
# if t <= 37 and w and p:
#     diagnosis = 'hay fever'
# elif s == 'Winter' and t > 37 and not h:
#     diagnosis = 'flu'
# elif t > 37 and not s == 'Winter':
#     diagnosis = 'a virus'
# else:
#     diagnosis = 'healthy'
# for testing:
# print(diagnosis) # should be 'a virus'

# Question 3b
# answer:
#0
#20
# for testing:
# def multiply(number):
#     p = number * 2
#     return p
#
# def testNumber(number):
#     result = 0
#     if(number >= 7 and number < 20):
#         result = multiply(number)
#     return result
#
# first_result = testNumber(5)
# print(first_result)
#
# second_result = testNumber(10)
# print(second_result)

# Question 4a
# answer:
# def getReply(msg, bannedReplies):
#     print(msg)
#     while True:
#         reply = input('Reply :')
#         if reply.lower() in [x.lower() for x in bannedReplies]:
#             print('Invalid response')
#         else:
#             return reply

# for testing:
# msg = 'reply: '
# bannedReplies = ['yes','no']
# print(getReply(msg='age?',bannedReplies=['yes','no']))

# Question 4b
# Learnings: calling a sub function within a function will not add the 'return' of the sub function to the function.
# Learnings: Instead, assign the sub function to a variable, then return the variable at the end of the function.
# testing:
# def getReply(msg, bannedReplies):
#     while True:
#         response = input(msg)
#         if response.lower() not in [x.lower() for x in bannedReplies]:
#             return response
# answer:
# def getReplyV2(msg, bannedWordlist, bannedWordListFilename=False):
#     if not bannedWordListFilename:
#         return getReply(msg,bannedWordlist)
#     else:
#         try:
#             newList = bannedWordlist[:]
#             with open(bannedWordListFilename,'r') as file:
#                 for line in file:
#                     word = line.strip()
#                     if word not in newList:
#                         newList.append(word)
#             return getReply(msg,newList)
#         except:
#             return getReply(msg,bannedWordlist)

# for testing:
# msg = 'Age: '
# bannedWordList = ['yes','no']
# with open('bannedWords.txt','w') as f:
#     f.writelines([x+'\n' for x in ['yeah','nah']])
# print(getReplyV2(msg, bannedWordList)) # should accept 'maybe'
# bannedWordListFilename = 'bannedWords.txt'
# print(getReplyV2(msg, bannedWordList, bannedWordListFilename)) # should not accept 'yeah' or 'nah'

# Question 4c
# Learnings: Make sure the dictionary contains all the necessary keys, it's easy to overlook the 'o' while entering 0 for each value.
# Learnings: .lower() is a built in function of strings, make sure it has the () included.
# for testing:
# wordlist = ['big','cats','like','really']
# answer:
# vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# for word in wordlist:
#     for ch in word:
#         for vowel in vowels:
#             if ch.lower() == vowel:
#                 vowels[vowel] += 1
# for vowel in vowels:
#     print('"{}" occurs {} times.'.format(vowel,vowels[vowel]))

# or...

# vowels = [['a', 0],['e',0],['i',0],['o',0],['u',0]]
# for word in wordlist:
#     for ch in word:
#         for vowel in vowels:
#             if ch.lower() == vowel[0]:
#                 vowel[1] += 1
# for vowel in vowels:
#     print('"{}" occurs {} times.'.format(vowel[0],vowel[1]))

# Question 5a
# answer:
# def float_check(msg):
#     while True:
#         response = input(msg)
#         if response == "":
#             return
#         else:
#             try:
#                 return float(response)
#             except:
#                 print('Invalid Number')
# for testing:
# msg = 'enter num: '
# print(float_check(msg))

# Question 5b
# for testing:
# with open('numbers.txt','w') as f:
#     f.write('3 2\n')
#     f.write('20 1\n')
#     f.write('5 100\n')
# answer:
# Learnings: When accessing numbers from a file, make sure to use int() or float() as appropriate to use them for subsequent calculations
# lines = 0
# sum = 0
# with open('numbers.txt','r') as f:
#     for line in f:
#         lines += 1
#         product = int(line.split()[0].rstrip()) * int(line.split()[1].rstrip())
#         sum += product
# print('There were {} lines'.format(lines))
# print('The total of the {} lines is {}'.format(lines,sum))

# Question 6a
# answer:
# Learnings: Think carefully about how to note the first line where a word was found: You are looking for a line in a list of lines, not a word in a list of lines.
# Learnings: The dictionary value will need to be a list, so it can hold two items. Then, the 'first line' will be the second value in that list.
# def createStats(s):
#     dict = {}
#     sList = s.split('\n')
#     for string in sList:
#         for word in string.split():
#             if word not in dict:
#                 dict[word] = [1,sList.index(string) + 1]
#             else:
#                 dict[word][0] += 1
#     return dict
# for testing:
# s = """mary had
# a little lamb with a
# blue fleece and
# it had a little blue eye"""
# print(createStats(s))

# Question 6b
# Learnings: To print something as a column, use {:>10} (justification direction and spaces in column).
# answer:
# def wordReport(s):
#     dict = createStats(s)
#     for key in dict:
#         print('Word {>:10} Count: {} First Line {}'.format(key,dict[key][0],dict[key][1]))
# for testing:
# s = """mary had
# a little lamb with a
# blue fleece and
# it had a little blue eye"""
# wordReport(s)

# Question 6c
# answer:
# def find_track(MP3List,word):
#     for entry in MP3List:
#         if word in entry[1]:
#             print('Artist: {:>10}, Track: {:>10}, Album: {:>10}'.format(entry[0],entry[1],entry[2]))
# for testing:
# MP3List = [['kanye west','monster','dark fantasy'],['BEP','my humps','monkey biz']]
# word = 'mon'
# find_track(MP3List,word)
# find_track(MP3List,word='my')
