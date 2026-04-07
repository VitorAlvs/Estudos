#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
x = 0
eve_nums = []

while x <= 15:
    if x%2 == 0:
        eve_nums.append(x)
    x += 1

#Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

accum = 0
x = 0
while accum != sum(list1):
    accum += list1[x]
    x+=1    

#Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(list1):
    new_list=[]
    i = 0
    while i < len(list1) :
        if list1[i] == 4 :
            break
        new_list.append(list1[i])
        i=i+1
            
    return new_list
