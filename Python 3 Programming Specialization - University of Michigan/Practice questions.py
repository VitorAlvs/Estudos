print(f"\n Write code to determine how many 9’s are in the list nums and assign that value to the variable how_many. Do not use a for loop to do this.")
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = 0

y = 0

while y < len(nums):
    if nums[y] == 9:
        how_many += 1
    y += 1

print(how_many)

print(f"\n Write code that uses iteration to print out the length of each element of the list stored in str_list.")
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for x in str_list:
    y = 0
    for z in x:
        y+=1
    print(y)
    
# print(f"\n Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.")
# op = open('emotion_words2.txt', 'r')    
# first_forty = op.read()[:40]

# print(f"\n Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.")
# op = open('emotion_words.txt', 'r')   
# num_lines = 0

# for each in op.readlines():
#     num_lines += 1

print(f"\n Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.")
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores = scores.split()
a_scores = sum(1 for x in scores if int(x) >= 90)

print(a_scores)