"""
A bunch of helper functions for analysis of text, utilized by an effective main.
The plan is to use it for feature engineering / quantitative insights on code.
"""

import string

def count_double_spaces(text):
    """
    number of occurrences of double spaces in the given text (thanks Dr. Han!)
    """
    words = text.split()
    count = sum([1 for w in words if '  ' in w])
    return count

  
def count_punctuation(text):
    """
    number of punctuation marks in the given text.
    """
    return sum([1 for c in text if c in string.punctuation])


def calculate_punct_density(text):
    """
    punctuation density (# of punctuation / len of text)
    """
    total_chars = len(text)
    punct_count = count_punctuation(text)
    return punct_count / total_chars


def count_exclamation_marks(text):
    """
    number of exclamation marks
    """
    return text.count('!')


def count_question_marks(text):
    """
    number of question marks
    """
    return text.count('?')


def calculate_exclamation_ratio(text):
    """
    ratio of exclamation marks to the total number of punctuation marks
    """
    punct_count = count_punctuation(text)
    exclamation_count = count_exclamation_marks(text)
    return exclamation_count / punct_count


def calculate_question_ratio(text):
    """
    ratio of question marks to the total number of punctuation marks
    """
    punct_count = count_punctuation(text)
    question_count = count_question_marks(text)
    return question_count / punct_count


def analyze(text):
    """
    returns everything
    """
    return {
        "punct_count": count_punctuation(text),
        "punct_density": calculate_punct_density(text),
        "exclamation_ratio": calculate_exclamation_ratio(text),
        "question_ratio": calculate_question_ratio(text),
        "double_spaces": count_double_spaces(text),
    }
