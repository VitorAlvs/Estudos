#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(x):
    sub = []
    i = 0
    while i < len(x):
        if x[i] == 5:
            break
        sub.append(x[i])
        i += 1
    return sub

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(x):
    i = 0
    list = []
    while i < len(x):
        if x[i] == 7:
            break
        list.append(x[i])
        i += 1
    return list   

#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(x):
    i = 0
    list = []
    while i < len(x):
        if x[i] == 'STOP':
            break
        list.append(x[i])
        i += 1
    return list   

#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(x):
    i = 0
    list = []
    while i < len(x):
        if x[i] == 'z':
            break
        list.append(x[i])
        i += 1
    return list   

    
#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
i = 0
while sum2 < sum(lst):
    sum2 += lst[i]
    i += 1
    
#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(x):
    i = 0
    list = []
    while i < len(x):
        if x[i] == 'bye':
            break
        list.append(x[i])
        i += 1
    if len(list) < 10:
        p = len(list)
        return list[:p]   
    else:
        return list[:10]