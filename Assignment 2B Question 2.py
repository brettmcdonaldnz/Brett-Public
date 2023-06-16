# By Brett McDonald
# SID: 10158931
# Assignment 2B
# Question 2: Text file statistics

fileOpen = open("Assignment 2B Question 2 Test File.txt","r") # open the file

statisticsFile = '' # initiate a string for copying the contents of the file to.

line_count = 0 # initiate line count
word_count = 0 # initiate word count
word_char_total = 0 # initiate the total number of characters per word for use with the word_char_average formula
letter_e_count = 0 # initiate the number of times the letter 'e' occurs in the file
replaceChars = [":",",",".","!","?"] # list for replacing punctuation for statistical purposes

for line in fileOpen:
    line_count += 1 # increment the line count
    statisticsFile += line # copy the file contents to statisticsFile

print(statisticsFile) # display the file

statisticsFile = statisticsFile.lower() # lower all characters in the file for statistical purposes

for char in replaceChars:
    statisticsFile = statisticsFile.replace(char," ") # remove punctuation for statistical purposes

for word in statisticsFile.split():
    word_count += 1 # increment the word count
    word_char_total += len(word) # increment the total word length for use with the word_char_average formula
    for char in word:
        if char == 'e':
            letter_e_count += 1 # count the number of times the letter 'e' occurs in the file

word_char_average = word_char_total / word_count # compute the average number of characters per word

print("There are {} lines in the file".format(line_count)) # display the line count

print("There are {} words in the file".format(word_count)) # display the word count

print("The average number of characters per word is {:.0f} (rounded to the nearest whole number)".format(word_char_average)) # display the average number of characters per word, rounded to the nearest whole number

print("The letter 'e' occurs in the file {} times".format(letter_e_count)) # display the letter 'e' count

fileOpen.close() # close the file

