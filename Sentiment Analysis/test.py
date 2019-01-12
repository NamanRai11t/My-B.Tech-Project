import csv

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

n_instances = 100
headlines = []
nltk.download('punkt')

with open('test_100.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for line in csv_reader:
        headlines.append(line[1])

print(headlines[2])

sentim_analyzer = SentimentAnalyzer()
headlines_copy = list(headlines)
headlines = []

for headline in headlines_copy:
    headlines.append(nltk.word_tokenize(headline))

all_words_neg = sentim_analyzer.all_words([mark_negation(headline) for headline in headlines])

print(all_words_neg[3])
