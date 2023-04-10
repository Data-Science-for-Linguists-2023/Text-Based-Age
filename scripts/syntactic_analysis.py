import spacy
import string
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def analyze_sentence_length(text):
    """
    tokenizes into sentences and returns list of lengths
    """
    doc = nlp(text)
    sentence_lengths = [len(sent) for sent in doc.sents]
    return sentence_lengths


def analyze_words(text):
    """
    tokenizes into words and returns the vocabulary size
    """
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    vocabulary_size = len(set(tokens))
    return vocabulary_size


def analyze_syntax(text):
    """
    tokenizes the given text into words
    applies POS tagging
    returns a dictionary containing frequency count of each tag
    """
    doc = nlp(text)
    tag_counts = Counter([token.pos_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space])
    return tag_counts


def analyze_caps(text):
    """
    tokenizes into words and identifies capitalized words
    """
    doc = nlp(text)
    capitalized_words = [token.text for token in doc if token.text.isupper() and not token.is_stop and not token.is_punct and not token.is_space]
    return capitalized_words


def word_freqs(text):
    """
    tokenizes into words and counts the frequency of each word
    """
    doc = nlp(text)
    words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    word_frequencies = dict(Counter(words))
    return word_frequencies


def analyze(text):
    """
    returns everything
    """
    return {
        "sentence_lengths": analyze_sentence_length(text),
        "vocabulary_size": analyze_words(text),
        "pos_tag_counts": analyze_syntax(text),
        "capitalized_words": analyze_caps(text),
        "word_frequencies": word_freqs(text)
    }
