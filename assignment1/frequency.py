import sys
import json

def get_tweets(tweetsfile):
    tweets_file = open(tweetsfile)
    tweets = []
    for tweet in tweets_file:
        json_tweet = json.loads(tweet)
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    tweets_str = ' '.join(tweets)
    return tweets_str

def create_terms(terms):
    unique_terms = []
    list_terms = terms.split()
    for term in list_terms:
        if term not in unique_terms: unique_terms.append(term)
    return unique_terms

def frequency(terms, tweets):
    terms_total = len(tweets.split())
    for term in terms:
        total = tweets.count(term)
        frequency = float(total)/float(terms_total)
        print term + " " + str(frequency)

def main():
    file_name = sys.argv[1]
    tweets = get_tweets(file_name)
    terms = create_terms(tweets)
    frequency(terms, tweets)

if __name__ == '__main__':
    main()
