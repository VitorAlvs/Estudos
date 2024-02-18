import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char
fileref = open("10-3Doc1.txt", "r")
read = fileref.read()

num_char = len(read)
print(num_char)

#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
fileref = open('10-3Doc2.txt', 'r')
lines = fileref.readlines()
num_lines = len(lines)

print(num_lines)

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
fileref = open("10-3Doc3.txt", "r")
read = fileref.read()
first_forty = read[:40]
print(first_forty)