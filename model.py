from time import strftime

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def log(msg):
    print('[{} model.py] {}'.format(strftime('%Y-%m-%d %H:%M:%S'), msg))

df = pd.read_csv('./spam_clean.csv')

tfidf = TfidfVectorizer()

X = tfidf.fit_transform(df.text)
y = df.label

log('Training model')
lm = LogisticRegression(solver='saga').fit(X, y)

log('Finished training model')
log('Accuracy: {:.2%}'.format(accuracy_score(y, lm.predict(X))))
log('Classification Report')
print(classification_report(y, lm.predict(X)))
log('All done')

def predict(msg):
    return lm.predict(tfidf.transform([msg]))[0]