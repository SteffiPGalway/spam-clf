import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.external.joblib as extjoblib
import joblib
from sklearn.model_selection import train_test_split #Validation split

df = pd.read_csv("spam.csv", encoding="latin-1")
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	
# Features and Labels
df['label'] = df['class'].map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label']
	
# Extract Feature With CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X) # Fit the Data
	
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	
#Naive Bayes Classifier
clf = MultinomialNB()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))

#Alternative Usage of Saved Model
joblib.dump(clf, 'NB_spam_model.pkl')
joblib.dump(cv, 'cv.pkl')
