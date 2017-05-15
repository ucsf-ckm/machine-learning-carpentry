from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
import re

train = pd.read_csv('data/trainReviews.tsv', header=0, delimiter="\t", quoting=3)

train_records = []

for i in range( 0, len(train["text"])):
    text = train["text"][i]
    text = re.sub("[^a-zA-Z0-9]"," ", text)
    train_records.append(text.lower())

vectorizer = CountVectorizer(analyzer = "word", 
    tokenizer = None, 
    preprocessor = None, 
    stop_words = 'english',                                
    max_features = 5000)

train_data_features = vectorizer.fit_transform(train_records)
train_data_features.toarray()
np.asarray(train_data_features)

clf = RandomForestClassifier()
#clf = MLPClassifier()
#clf = MultinomialNB()
#clf = LogisticRegression()
#clf = SVC()
clf.fit( train_data_features, train["category"] )

test = pd.read_csv('data/testReviews.tsv', header=0, delimiter="\t", quoting=3)

test_records = [] 
    
for i in range(0,len(test["text"])):
    text = test["text"][i]
    text = re.sub("[^a-zA-Z0-9]"," ", text)
    test_records.append(text.lower())

test_data_features = vectorizer.transform(test_records)
np.asarray(test_data_features)

predictions = clf.predict(test_data_features)

prediction_list = pd.DataFrame( data={"id":test["id"], "category":predictions} )

print(1 - float(sum(abs(prediction_list['category'] - test['category']))) / float(len(test['category'])))



