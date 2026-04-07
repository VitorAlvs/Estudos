#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []

for each in verbs:
    newVerb = each[:] + "ing"
    ing.append(newVerb)

print(ing)

#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist>.
numbs = [5, 10, 15, 20, 25]
newlist = []

for each in numbs:
    newlist.append(each + 5)

print(newlist)

#Given the list of numbers, numbs, modifiy the list numbs> so that each of the original numbers are increased by 5. Note this is not an accumulator pattern problem, but its a good review.
numbs = [5, 10, 15, 20, 25]
x = 0

for each in numbs:
    numbs[0] = each + 5
    x += 1
    print(x)

numbs.sort()
print(numbs)

#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []

for each in lst_nums:
    larger_nums.append(each * 2)

print(larger_nums)