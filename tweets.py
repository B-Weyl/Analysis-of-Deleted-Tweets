import csv
import matplotlib.pyplot as plt
import re
import string
from collections import Counter, defaultdict
from stop_words import get_stop_words
import fnmatch


def get_unique_usernames():
    # create a set of all the unique usernames that tweeted
    usernames = set()
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['user_key']:
                usernames.add(row['user_key'])
    return usernames


def get_total_usernames():
    # create a set of all the unique usernames that tweeted
    total_usernames = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['user_key']:
                total_usernames.append(row['user_key'])
    return total_usernames


def get_top_ten_users():
    # create a set of all the unique usernames that tweeted
    total_usernames = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['user_key']:
                total_usernames.append(row['user_key'])
    d = defaultdict(int)
    # create a dict of mentioned user and times mentioned
    for i in total_usernames:
        d[i] += 1
    top_ten = dict(Counter(d).most_common(10))
    return top_ten


def get_hashtags():
    # create a set of all the unique hashtags that were used
    hashtags = set()
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['hashtags'] != '[]' and len(row['hashtags']) > 1:
                hts = row['hashtags'].split(',')
            else:
                hashtags.add(row['hashtags'].strip('[]').lower())
            for ht in hts:
                hashtags.add(ht.strip('[]').lower())
    return hashtags


def get_mentioned_users_unique():
    # create a set of unique users that were mentioned in tweets
    unique_mentioned_users = set()
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['text']:
                # divide the text into a list of words
                tweet_text = row['text'].split(' ')
                for word in tweet_text:
                    if word.startswith('@'):
                        # remove characters that would be illegal in a username
                        word = re.sub('[^A-Za-z0-9 ]+', '', word)
                        unique_mentioned_users.add(word.strip(''))

    return unique_mentioned_users


def get_mentioned_users_total():
    total_mentioned_users = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['text']:
                # divide the text into a list of words
                tweet_text = row['text'].split(' ')
                for word in tweet_text:
                    if word.startswith('@'):
                        # remove characters that would be illegal in a username
                        word = re.sub('[^A-Za-z0-9 ]+', '', word)
                        total_mentioned_users.append(word.strip(''))
    return total_mentioned_users


def get_top_ten_mentioned_users():
    total_mentioned_users = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['text']:
                # divide the text into a list of words
                tweet_text = row['text'].split(' ')
                for word in tweet_text:
                    if word.startswith('@'):
                        # remove characters that would be illegal in a username
                        word = re.sub('[^A-Za-z0-9 ]+', '', word)
                        total_mentioned_users.append(word.strip(''))
        d = defaultdict(int)
        # create a dict of mentioned user and times mentioned
        for i in total_mentioned_users:
            d[i] += 1
    # get the top # of users mentioned in
    top_ten = dict(Counter(d).most_common(10))
    return top_ten


def graph_top_ten_menitoned(d):
    plt.figure(figsize=(15, 5))
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.ylabel("Number of times mentioned in tweets")
    plt.xlabel("User mentioned in tweets")
    plt.show()


def graph_top_ten_users(d):
    plt.figure(figsize=(15, 5))
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.ylabel("Number of times tweeted")
    plt.xlabel("User that tweeted")
    plt.show()


def get_banned_users():
    # create a set of all the unique usernames that tweeted
    banned_users = set()
    with open('users.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['screen_name']:
                banned_users.add(row['screen_name'])
    return banned_users


def cross_reference_users_to_banned():
    banned_users = get_banned_users()
    total_users = get_unique_usernames()
    return list(set(total_users) - set(banned_users))


def cross_reference_mentioned_users_to_banned():
    banned_users = get_banned_users()
    total_mentioned_users = get_mentioned_users_unique()
    return list(set(total_mentioned_users) - set(banned_users))


def print_info():
    print("There were {} total users that tweeted".format(
        len(get_total_usernames())))
    print("Subtracting the {} users in the banned users doc, we are left " +
          "with {} users".format(
              len(get_banned_users()),
              (len(get_total_usernames()) - len(get_banned_users()))))


def user_reach(username):
    # determine how many other users the given user reached out to or
    # was contacted by ; in a way to determine their influence.
    # ie how many people did they make an "impression" on
    count = 0
    relations = []
    d = {}
    # todo - figure out a way to determine influence of an account
    return


def every_word():
    total_words = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['text']:
                # divide the text into a list of words
                tweet_text = row['text'].split(' ')
                for word in tweet_text:
                    word = re.sub('[^A-Za-z0-9 ]+', '', word)
                    total_words.append(word)
    d = defaultdict(int)
    # create a dict of mentioned user and times mentioned
    stop_words = generate_stop_words()
    for i in total_words:
        if i.lower() not in stop_words:
            d[i] += 1
    top_twenty_five = dict(Counter(d).most_common(25))
    print(len(total_words))

    return top_twenty_five


def generate_stop_words():
    stop_words = list(get_stop_words('en'))
    exclude = [
        'im', 'https', 'httpst', 'httpstco', 'tcot', 'dont', 'cant', 'amp',
        'RT', 'via', 'us', 'can', 'one', 'go', 'http', 'go', 'going', 'just',
        '', '2', 'get'
    ]
    stop_words.extend(exclude)
    stop_words = [x.lower() for x in stop_words]
    return stop_words


def graph_top_twenty_five_words(d):
    plt.figure(figsize=(25, 5))
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.ylabel("Number of times word used")
    plt.xlabel("Word")
    plt.show()


def get_top_hashtags():
    total_hashtags = []
    with open('tweets.csv') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if row['hashtags'] != '[]' and len(row['hashtags']) > 1:
                hts = row['hashtags'].split(',')
            else:
                total_hashtags.append(row['hashtags'].strip('[]').lower())
            for ht in hts:
                total_hashtags.append(ht.strip('[]').lower())
    d = defaultdict(int)
    # create a dict of mentioned user and times mentioned
    for i in total_hashtags:
        if i.lower() != '' and i != '"tcot"' and i != '"ccot"':
            d[i] += 1
    top_twenty_hashtags = dict(Counter(d).most_common(20))
    return top_twenty_hashtags


def main():
    # graph_top_twenty_five_words(every_word())
    # print(get_top_hashtags())
    # print(len(get_hashtags()))
    # print(len(get_unique_usernames()))
    # print(len(get_mentioned_users_unique()))
    # print(get_top_ten_mentioned_users())
    print(len(every_word()))


if __name__ == '__main__':
    main()