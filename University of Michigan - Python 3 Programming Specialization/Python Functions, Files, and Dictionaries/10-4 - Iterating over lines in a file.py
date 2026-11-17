import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#To make the code a little simpler, and to allow for more efficient processing, Python provides a built-in way to iterate through the contents of a file one line at a time, without first reading them all into a list. Some students find this confusing initially, so we don’t recommend doing it this way, until you get a little more comfortable with Python. But this idiom is preferred by Python programmers, so you should be prepared to read it. And when you start dealing with big files, you may notice the efficiency gains of using it.

olypmicsfile = open("10-4Doc1.txt", "r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
emotionfile = open("10-3Doc3.txt", "r")
lines = emotionfile.readlines()
num_lines = 0

for each in lines:
    num_lines += 1

print(lines)
print(num_lines)