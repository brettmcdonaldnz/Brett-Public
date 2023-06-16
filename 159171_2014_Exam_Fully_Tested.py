# Answers and Learnings from 159.171 Exam 2014.
# I've tested all of the answers, and they would achieve full marks as far as I can tell.

# Question 1a
# answer
#74
#error - can't add types int and string
#3737
# for testing:
# print(37 + 37)
# print (37 + '37')
# print ('37' + '37')

# Question 1b
# for testing:
# name = 'Sue'
# age = 20
# height = 1.7214
# answer:
# print('{} is {} and is {:.2f}m tall'.format(name,age,height))

# Question 2a
# answer:
# count = 1
# while count < 251:
#     print(count)
#     count += 7

# Question 2b
# answer:
# count = 1
# while count < 251:
#     if 100 <= count <= 105 or 200 <= count <= 205:
#        print('Excluded')
#     else:
#        print(count)
#     count += 7

# Question 3
# for testing:
# temperature = 39
# spots = False
# blockedNose = True
# wateryEyes = False
# season = 'winter'
# answer:
# Learnings: be careful when abbreviating variable names, that you don't use the same variable name twice (like 's' for spots and 's' for season)
# t = temperature
# s = spots
# b = blockedNose
# w = wateryEyes
# sea = season
# if 36 <= t <= 38 and (b or w) and (sea == 'spring' or sea == 'summer'):
#     diagnosis = 'hay fever'
# elif s and t > 38:
#     diagnosis = 'measles'
# elif b and t > 38:
#     diagnosis = 'flu'
# else:
#     diagnosis = 'healthy'
# for testing:
# print(diagnosis) # should be 'flu'

# Question 4a
# answer:
# def getReply(msg, validReplies):
#     while True:
#         response = input(msg)
#         if response in validReplies:
#             return response
# for testing:
# msg = 'yes or no'
# validReplies = ['yes','no']
# print(getReply(msg,validReplies))

# Question 4b
# answer:
# def getReplyV2(msg, validReplies, maxTries):
#     count = 0
#     while count < maxTries:
#         response = input(msg)
#         if response in validReplies:
#             return response
#         count += 1
#     return

# returned_value = getReplyV2(msg='yes or no: ', validReplies = ['yes','no'], maxTries = 5)
# if returned_value:
#     print(returned_value)
# else:
#     print('No valid reply')
# for testing: run the code above with 'x' 5 times, it should print 'no valid reply',
# then run it with 'yes', it should print 'yes'

# Question 5a
# answer:
# def countWords(thisWord, listOfWords):
#     count = 0
#     for word in listOfWords:
#         if word == thisWord:
#            count += 1
#     return count
# for testing:
# print(countWords(thisWord='cat', listOfWords=['cat','cats','dog','dogs'])) # should print '1'

# Question 5b
# answer:
# def countWordsV2(targetWords, listofWords):
#     for word in targetWords:
#         print('"{}" occurs {} times.'.format(word,countWords(word, listofWords)))
# for testing:
# def countWords(thisWord, listOfWords):
#     count = 0
#     for word in listOfWords:
#         if word == thisWord:
#             count += 1
#     return count
# countWordsV2(targetWords=['frog','really','fish','big'], listofWords = ['big','cats','like','really','really','really','big','fish'])
# should display:
# "frog' occurs 0 times.
# "really" occurs 3 times.
# "fish" occurs 1 times.
# "big" occurs 2 times.

# Question 6a
# answer:
# 165
# 50
# checked online, these values are correct

# Question 6b
# answer:
# r = input('Enter a floating number: ')
# try:
#     r = float(r)
#     print(r)
# except:
#     print('Invalid Number')
# for testing: run the above code with 'x' - should print 'Invalid Number',
# and with '9', should print 9.0, and with 9.56, should print 9.56

# Question 6c
# Learnings: be careful with builtin string functions; lstrip should be written as lstrip()
# for testing:
# with open('in.txt','w') as intxt:
#     intxt.writelines(['line 1\n','\n',' # line 3\n', 'line 4\n'])
# answer:
# with open('in.txt','r') as intxt, open('out.txt','w') as outtxt:
#     for line in intxt:
#         if line != "\n" and line.lstrip()[0] != '#':
#             outtxt.write(line)
# for testing: read the file 'out.txt', it should only have two lines: 'line 1' and 'line 4'

# Question 8a
# for testing:
# fruitInStock = {'apples':1, 'oranges':2, 'pears':3}
# answer:
# fruitInStock['bananas'] = 4
# for testing:
# print(fruitInStock)

# Question 8b
# for testing:
# fruitInStock = {'apples':1, 'oranges':2, 'pears':3, 'bananas':4}
# answer:
# fruitInStock['apples'] = fruitInStock['pears']
# for testing:
# print(fruitInStock)

# Question 8c
# answer:
# print(key in dict) # this will print True if the key is in the dictionary, otherwise it will print False.
# for testing:
# fruitInStock = {'apples':1, 'oranges':2, 'pears':3, 'bananas':4}
# print('apples' in fruitInStock) # should print True
# print('apple' in fruitInStock) # should print False

# Question 9a and 9b
# Learnings: be extra careful with builtin string methods inside of other methods, it's easy to forget to write .strip as .strip() when it is inside a .append()
# Learnings: when using a disposable subList variable, redeclare it as an empty list for each iteration as required, rather than modifying a global subList (which causes complications)
# for testing:
# with open('CSV.txt','w') as csv:
#     csv.write('1010,Bill,145.98\n1147,Gina,10288.97\n2917, Willie, 4.97')
# answer:
# entries = {}
# listOfLists = []
# with open('CSV.txt','r') as csv:
#     for line in csv:
#         subList = []
#         for item in line.split(','):
#             if item.strip().isdigit():
#                 subList.append(int(item.strip()))
#             else:
#                 try:
#                     subList.append(float(item.strip()))
#                 except:
#                     subList.append(item.strip())
#         if subList[1] not in entries:
#            entries[subList[1]] = subList
#         listOfLists.append(subList)
# for testing:
# print(entries) # should print entries for Bill, Gina and Willie
# print(entries['Gina']) # should print entry for Gina
# print(listOfLists) # should print listOfLists
# print(entries['Gina'][0]*entries['Gina'][2]) # should print 11801448.59


