#importing the libraries

#importing nltk
import nltk 

#importing stemming library
from nltk.stem.lancaster import LancasterStemmer
#creating object for stemming
stemmer = LancasterStemmer()

#importing numpy, tflearn, tensorflow, random, json
import numpy
import tflearn
import tensorflow
import random
import json

#stopwords helps us to remove the words like 'for', 'then', 'from', 'and' which are repeting again and again
#which does not put much value to identify sentance
from nltk.corpus import stopwords

#Getting all the data from json file
with open("intents.json") as file:
    data = json.load(file)

#Printing the data for checking purposes
# print(data)
#TEST PASS

#creating the list of all words in json file
words = []

for intentPattern in data["intents"]:
    for pattern in intentPattern["patterns"]:
        words = nltk.word_tokenize(pattern)
        words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
        patterns = ' '.join(words) 
        print(patterns)