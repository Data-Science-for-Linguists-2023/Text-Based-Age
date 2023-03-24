import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def analyze_sentence_length(text):
    """
    tokenizes into sentences and returns list of lengths
    """
    sentences = sent_tokenize(text)
    sentence_lengths = [len(sent) for sent in sentences]
    return sentence_lengths


def analyze_words(text):
    """
    tokenizes into words and returns the vocabulary size (lemmatization and stopword removal)
    need to experiment with lemmatize and stopword removal -> they might actually be relevant features
    """
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(text) if token.lower() not in stopwords.words('english') and token not in string.punctuation]
    vocabulary = set(tokens)
    return len(vocabulary)


def analyze_syntax(text):
    """
    tokenizes the given text into words
    applies POS tagging
    returns a dictionary containing frequency count of each tag
    """
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(text) if token.lower() not in stopwords.words('english') and token not in string.punctuation]
    tags = nltk.pos_tag(tokens)
    tag_counts = {}
    for tag in tags:
        if tag[1] not in tag_counts:
            tag_counts[tag[1]] = 1
        else:
            tag_counts[tag[1]] += 1
    return tag_counts

def analyze_caps(text):
    """
    tokenizes into words and identifies capitalized words
    """
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(text) if token.lower() not in stopwords.words('english') and token not in string.punctuation]
    capitalized_words = [word for word in tokens if word[0].isupper()]
    return capitalized_words

def word_freqs(text):
    """
    tokenizes into words and counts the frequency of each word
    """
    vectorizer = CountVectorizer(stop_words='english')
    doc_term_matrix = vectorizer.fit_transform([text])
    word_frequencies = np.asarray(doc_term_matrix.sum(axis=0))
    word_frequencies = dict(zip(vectorizer.vocabulary_, word_frequencies[0]))
    return word_frequencies



def analyze(text):
    """
    Analyzes the given text and returns a dictionary containing the results of various analysis functions.
    """
    return {
        "sentence_lengths": analyze_sentence_length(text),
        "vocabulary_size": analyze_words(text),
        "pos_tag_counts": analyze_syntax(text),
        "capitalized_words": analyze_caps(text),
        "word_frequencies": word_freqs(text)
    }