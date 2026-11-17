#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
opens   = open('travel_plans.txt', 'r')
num     = len(opens.read())

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words
opens = open('emotion_words.txt','r')
reads = opens.read()
num_words =len(reads.split())

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
opens = open('school_prompt.txt','r')
num_lines = len(opens.readlines())

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
opens = open('school_prompt.txt','r')
beginning_chars = opens.read()[:30]

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
opens = open('school_prompt.txt','r')
lines = opens.readlines()

three = []

for each in lines:
    each = each.split()
    three.append(each[2])

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
opens = open('emotion_words.txt','r')
lines = opens.readlines()

emotions = []

for each in lines:
    each = each.split()
    emotions.append(each[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
opens = open('travel_plans.txt','r')
first_chars = opens.read()[:33]

#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
opens = open('school_prompt.txt','r')
reads = opens.read()
words = reads.split()
p_words = []

for each in words:
    if 'p' in each:
        p_words.append(each)


