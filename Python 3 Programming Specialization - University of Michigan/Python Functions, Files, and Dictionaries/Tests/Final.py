# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


#Positive words
positive_wrds = []
with open('positive_words.txt', 'r') as pstv:
    for each in pstv:
        if each[0] != ';' and each[0] != '\n':
            positive_wrds.append(each.strip())
print(positive_wrds)

#Negative words
negative_wrds = []
with open('negative_words.txt', 'r') as pstv:
    for each in pstv:
        if each[0] != ';' and each[0] != '\n':
            negative_wrds.append(each.strip())
print(negative_wrds)

#Def pstv score
def pstv_score(x):
    y = 0
    for each in x:
        if x in positive_wrds:
            y += 1
    return y

#Def negt score
def negt_score(x):
    y = 0
    for each in x:
        if x in negative_wrds:
            y += 1
    return y

#Tweets
tweets_lst = []
with open('project_twitter_data.csv', 'r') as file:
    lines = file.readlines()
    for each in lines[1:]:
        each = each.strip().split(',')
        retweet_count = each[1]
        reply_count = each[2]
        positive_score = pstv_score(each)
        negative_score = negt_score(each)
        y = retweet_count, reply_count, positive_score, negative_score
        tweets_lst.append(y)
print(tweets_lst)


