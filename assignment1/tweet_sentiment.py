import sys
import json
   
def main():
   
    tweet = []
     
    with open(sys.argv[2],"r") as j:
        for i in j:
            tweet.append(json.loads(i))
     
    texts = []
    for i in tweet:
        if "text" in i:
            texts.append(i["text"].split())
     
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
     
    sentiments = []
    for i in texts:
        sentiment = 0
        for j in i:
            if (j.lower()) in scores:
                sentiment += scores[j.lower()]
        sentiments.append(sentiment,1)
    
    for i in sentiments:
	print i

if __name__ == '__main__':
    main()
