# -*- coding: utf-8 -*-
from typing import List
from pythainlp.tokenize import Tokenizer
from laonlp.corpus import lao_words

_word = Tokenizer(lao_words(), engine="mm")


def word_tokenize(sent: str) -> List[str]:
    """
    Lao word tokenize

    :param str sent: lao text
    :return: returns a list of lao words
    :rtype: list
    """
    return _word.word_tokenize(sent)


def sent_tokenize(txt: str) -> List[str]:
    """
    Sentence tokenizer.

    Lao Text to sentence

    :param str sent: lao text
    :return: returns a list of lao sentence
    :rtype: list
    """
    return txt.split(".")
