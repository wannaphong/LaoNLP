# -*- coding: utf-8 -*-
__all__ = [
    "word_dictionary",
]

def word_dictionary(word: str, src: str, target: str, name: str = "mopt_laos")->list:
    from laonlp.translate.mopt_dict import dictionary
    return dictionary(word, src, target)