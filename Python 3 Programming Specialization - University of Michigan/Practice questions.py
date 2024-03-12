#Write code to determine how many 9’s are in the list nums and assign that value to the variable how_many. Do not use a for loop to do this.
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = 0

y = 0

while y < len(nums):
    if nums[y] == 9:
        how_many += 1
    y += 1

#Write code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for x in str_list:
    y = 0
    for z in x:
        y+=1
    print(y)
    
#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
op = open('emotion_words2.txt', 'r')    
first_forty = op.read()[:40]

#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
op = open('emotion_words.txt', 'r')   
num_lines = 0

for each in op.readlines():
    num_lines += 1