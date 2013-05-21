import sys
import json

def get_hashtags(tweetfile):
    tweets_file = open(tweetfile)
    hashtags = []
    for i in tweets_file:
        j = json.loads(i)
        if "entities" in j.keys():
            if j["entities"]["hashtags"] != []:
                for x in j["entities"]["hashtags"]:
                    if x["text"].isalnum():
                        hashtags.append((x["text"]))
    #print hashtags
    #print len(hashtags)
    count_list = {}
    for i in hashtags:
        if i in count_list:
            count_list[i] += 1
        else:
            count_list[i] = 1
    top_ten = []
    for i in sorted(count_list, key=count_list.get, reverse=True):
        top_ten.append((i, count_list[i]))
    top_ten = top_ten[0:10]
    for (x,y) in top_ten:
        print x + " " + str(y)
    #for i in sorted(count_list):
        #sortedlist = sorted(count
        #for j in range(10)
            #top_ten.append        
    #print top_ten


def main():
    file_name = sys.argv[1]
    hash_tags = get_hashtags(file_name)

if __name__ == '__main__':
    main()
