from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_classifier(texts, labels):
    # create a CountVectorizer with character-based bigrams
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(2,2))
    X = vectorizer.fit_transform(texts)
    # train the classifier and return it
    clf = MultinomialNB()
    clf.fit(X, labels)
    return clf, vectorizer

def predict_age_group(classifier, vectorizer, new_text):
    # take in a classifier as input and return the prediction
    new_X = vectorizer.transform([new_text])
    predicted_age_group = classifier.predict(new_X)
    return predicted_age_group
