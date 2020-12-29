#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from typing import List
from nltk import PorterStemmer
from Lab7_get_vocabulary_dict import get_vocablist

def split(delimiters, string, maxsplit=0):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, string, maxsplit)

def process_email(email_contents: str) -> List[int]:
    """Pre-process the body of an email and return a list of indices of the
    words contained in the email.

    :param email_contents: the body of an email
    :return: a list of indices of the words contained in the email
    """

    # Load the vocabulary.
    vocab_list = get_vocablist()

    email_contents = email_contents.lower()
    email_contents = re.sub('<[^<>]+>', ' ', email_contents)
    email_contents = re.sub('[0-9]+', 'number', email_contents)
    email_contents = re.sub('(http|https)://[^\s]*', 'httpaddr', email_contents)
    email_contents = re.sub('[^\s]+@[^\s]+', 'emailaddr', email_contents)
    email_contents = re.sub('[$]+', 'dollar', email_contents)

    words = split(""" @$/#.-:&*+=[]?!(){},'">_<;%\n\r""", email_contents)
    word_indices = []
    stemmer = PorterStemmer()
    for word in words:
        word = re.sub('[^a-zA-Z0-9]', '', word)
        if word == '':
            continue
        word = stemmer.stem(word)
        print
        word,
        if word in vocab_list:
            idx = vocab_list.index(word)
            word_indices.append(idx)

    return word_indices
