# -*- coding: utf-8 -*-
from pythainlp.tokenize import Tokenizer
from laonlp.corpus import lao_words

_word = Tokenizer(lao_words(), engine="mm")

def word_tokenize(sent:str)->list:
    """
    Lao word tokenize

    :param str sent: lao text
    :return: returns a list of lao words
    :rtype: list
    """
    return _word.word_tokenize(sent)

def sent_tokenize(txt:str)->list:
    """
    Sentence tokenizer.

    Lao Text to sentence

    :param str sent: lao text
    :return: returns a list of lao sentence
    :rtype: list
    """
    return txt.split(".")