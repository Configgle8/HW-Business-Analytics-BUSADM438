from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def read_corpus_sentiment(filename):
    with open(filename) as file:
        #txt
        corpus = []
        #numlbl
        y = []
        for line in file:
            sentence, sentiment = line.strip().rsplit('\t', 1)
            corpus.append(sentence)
            y.append(int(sentiment))
        return corpus, y

#start read def
corpus_train, y_train = read_corpus_sentiment('HW5/yelp_labelled_train.txt')
corpus_test, y_test = read_corpus_sentiment('HW5/yelp_labelled_test.txt')

#lowercase & pre-processing
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X_train = vectorizer.fit_transform(corpus_train)
X_test = vectorizer.transform(corpus_test)

model = LogisticRegression()
model.fit(X_train, y_train)

#EVAL
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

#Print accuracy
print(accuracy)
