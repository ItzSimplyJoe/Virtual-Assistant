import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from io import StringIO
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

class IntentClassifier: ### Makes use of naive bayes classifier algorithm
    def __init__(self):
        self.data = pd.read_csv('intentclassification/data.csv')
        self.train()

    def train(self):
        X_train, y_train= self.data['text'], self.data['intent']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        self.svm = LinearSVC().fit(X_train_tfidf, y_train)
    
    def predict(self, text):
        self.filecheck(text)
        return self.svm.predict(self.count_vect.transform([text]))[0]


    def filecheck(self,text):
        total = 0
        with open ('intentclassification/data.csv') as f:
            reader = csv.reader(f, delimiter=',')
            intent = self.svm.predict(self.count_vect.transform([text]))[0]
            data = (text+","+intent)
            for row in reader:
                for field in row:
                    if field == text:
                        total = 1
                        break
            if total == 0:
                file = open('intentclassification/data.csv', 'a')
                writer = csv.writer(file)
                list = [text,intent]
                writer.writerow(list)
                file.close()



intent_classifier = IntentClassifier()