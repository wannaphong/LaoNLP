# -*- coding: utf-8 -*-
__all__ = [
    "word_dictionary",
]

def word_dictionary(word: str, src: str, tarng: str, name: str = "mopt_laos"):
    from laonlp.translate.mopt_dict import dictionary
    return dictionary(word, src, tarng)