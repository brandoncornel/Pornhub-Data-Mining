import json
import os
import math
import operator

dir = os.path.dirname(__file__)

folderPath ="data/"
badWords={
    "the",
    "you",
    "so",
    "my",
    "me",
    "is",
    "i",
    "and",
    "your",
    "very",
    "to",
    "i",
    "a",
    "that",
    "it",
    "in",
    "of",
    "on",
    "are",
    "this",
    "want",
    "for",
    "can",
    "be"

}

class Main:

    def main(self):
        fileName = os.path.join(dir, folderPath+"comments.json")
        i = 0
        comments = {}
        with open(fileName) as json_data:
            for line in json_data:
                split_comment = []
                split_comment = line[line.find("\"text\"")+9:line.find("\"",line.find("\"text\"")+9)].split(" ")
                for comment_word in split_comment:
                    if(len(comment_word)>0 and comment_word.lower() not in badWords):
                        if(comment_word.lower() not in comments):
                            comments[comment_word.lower()] = 1
                        else:
                            comments[comment_word.lower()]+=1
        listNum = 30
        j = listNum
        for k,v in sorted(comments.items(), key=operator.itemgetter(1)):
            if(i>=(len(comments)-listNum)):
                print(j,":",k,"=",v)
                j-=1
            i+=1

Main().main()
