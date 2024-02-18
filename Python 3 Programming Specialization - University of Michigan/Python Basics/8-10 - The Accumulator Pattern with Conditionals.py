#For each string in the list words, find the number of characters in the string. If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.
words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0

for each in words:
    if type(each) == str:
        if len(each) > 3:
            num_words += 1

print(num_words)

#For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for each in words:
    if each[-1] == "e":
        past_tense.append(each+"d")
    else:
        past_tense.append(each+"ed")

print(past_tense)
