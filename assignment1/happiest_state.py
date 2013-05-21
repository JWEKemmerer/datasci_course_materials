import sys
import json

def tweet_information(tweetsfile):
    tweets_file = open(tweetsfile)
    tweets = []
    for tweet in tweets_file:
        json_tweets = json.loads(tweet)
        if "text" in json_tweets.keys():
            #if "lang" in json_tweets.keys():
                #if json_tweets["lang"] == 'en':
                    if not json_tweets["place"] == None:
                        if json_tweets["place"]["country_code"] == 'US':
                            state = json_tweets["place"]["full_name"].split(", ")[1]
                            if len(state) == 2 and state != 'US' and state != 'DC':
                                text = json_tweets["text"].encode('utf-8')
                                tweets.append((text,state))
    return tweets

def init_dict(sentimentfile):
    sentiment_file = open(sentimentfile)
    scores = {}
    for i in sentiment_file:
        terms, score = i.split("\t")
        scores[terms] = int(score)
    return scores

def calc_state(tweets,scores):
    states = {}
    for (tweet,state) in tweets:
        val = 0
        for score in scores:
            if (score.lower()) in tweet:
                val += scores[score.lower()]
                if state in states:
                    states[state] += val
                else:
                    states[state] = val
    #for key in sorted(states.keys()):
        #print key, states[key]
    final_state_value = 0
    final_state = " "
    for key in sorted(states.keys()):
        if states[key] > final_state_value:
            final_state_value = states[key]
            final_state  = key
    print final_state
            
def main():
    tweets_name = sys.argv[2]
    sentiment_name = sys.argv[1]
    tweets = tweet_information(tweets_name)
    dictionary = init_dict(sentiment_name)
    calc_state(tweets,dictionary)
if __name__ == '__main__':
    main()
