# -*- coding: utf-8 -*-
__all__ = [
    "word_dictionary",
]
from laonlp.translate.mopt_dict import dictionary

def word_dictionary(word: str, src: str, target: str, name: str = "mopt_laos")->list:
    """
    Word dictionary

    :param str word: text
    :param str src: src language (lao is Lao, eng is English)
    :param str name: Word dictionary (the default dict is mopt_laos.)
    :return: return word
    :rtype: str
    """
    return dictionary(word, src, target)