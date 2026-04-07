#For each character in the string already saved in the variable str1, add each character to a list called chars.
str1 = "I love python"
chars = []
for each in str1:
    chars.append(each)

print(chars)

#Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
output = ""

for each in range(1,36):
    output = output + "a"

print(output)