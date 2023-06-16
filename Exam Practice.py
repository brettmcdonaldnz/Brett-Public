# # Let's look at the question one step at a time:
#
# # 1. Write the function createStats(s)
# # 2. that takes a multi-line string (s)
# # 3. and builds a dictionary
# # 4. indexed by word,
# # 5. that contains the count
# # 6. and first line information.
#
# # After thinking through these steps, you can tell they are out of computational order (as is usually the case for these questions), so let's fix that:
#
# # 1. Write the function createStats(s)
# # 2. It will build a dictionary
# # 3. The dictionary is based on a multi-line string
# # 4. The dictionary will be indexed by word
# # 5. The dictionary index will contain the values of that word count and the first line it appeared.
#
# # Okay, now we can build the function:
#
# def createStats(s): # Step 1 is just following the exact instruction.
#
#     dict = {} # Step 2 is just adding the empty dictionary to build out later.
#
#     for line in s.split('\n'): # Step 3 is setting up iteration over a multi-line string ('multi-line' is a hint that we'll need to use .split('\n')).
#
#         for word in line.split(): # Step 4 is splitting the line into a list of words...
#
#             if word not in dict: # ... then checking if key already exists (key not in dict is the simple way), and either adding it or incrementing it.
#
#                 dict[word] = [1,s.split('\n').index(line)+1] # Step 5 is the most mentally challenging. We need a default value for when the word is added to the dictionary,
#                                    # and there are many ways of thinking it through. Here, I've thought, 'the dict needs two values [word,linecount], so
#                                    # so I can hold them in a list, and then update that list later as the word count increments. The word value is easy (it is 1 the first time
#                                    # that the word appears, we'll increment it later). The line count is trickier: it will be the index of where that line appears in the list of lines...
#                                    # But hold on, the question names the first line as '1', so I'll need to add 1 to that value.
#             else:
#
#                 dict[word][0] += 1 # This fulfills the other party of Step 5 (word count)
#
#     return dict # Lastly, the function will need to return the dict.
#
# # From there, Question 6b is relatively straightforward (but again, it's slightly out of computational order).
#
# # 1. "Write the function wordReport()
# # 2. that displays the report,
# # 3. using the dictionary created in part (a)."
#
# # So let's order it computationally:
#
# # 1. Write the function wordReport()
# # 2. Using the dictionary created in part (a)
# # 3. That displays the report.
#
# def wordReport(s): # Step 1 is just following the instruction again, but we'll need to add a parameter so it 'uses the dictionary created in part a' (there are other ways of handling that, but I chose to use a parameter).
#
#     report = createStats(s) # Step 2 is not entirely clear on how we should 'use the dictionary', so this is just the way I wanted to use it. There are other options.
#
#     for key in report: # Step 3: 'Display the report' means to use a print statement. We are going to try to follow the example given in the question; it appears to have some right-justification for the words.
#
#         print('Word {:>10} Count: {} First Line {}'.format(key,report[key][0],report[key][1])) # The arguments are based on my dict values as a list, so list[0] was the word count and list[1] was the first line count
#
#         # And that's the end of the question, and in the exam I'll just cross my fingers and move on. But here is the testing portion for PyCharm:

def createStats(s):
    dict = {}
    for line in s.split('\n'):
        for word in line.split():
            if word not in dict:
                dict[word] = [1,s.split('\n').index(line)+1]
            else:
                dict[word][0] += 1
    return dict

def wordReport(s):
    report = createStats(s)
    for key in report:
        print('Word {:>10} Count: {} First Line {}'.format(key,report[key][0],report[key][1]))


s = """mary had
a little lamb with a
blue fleece and
it had a little blue eye"""
wordReport(s)
