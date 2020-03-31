# -*- coding: utf-8 -*-
from pythainlp.tokenize import Tokenizer
from laonlp.corpus import lao_words

_word = Tokenizer(lao_words(), engine="mm")

def word_tokenize(sent):
    return _word.word_tokenize(sent)

def sent_tokenize(txt):
    return txt.split(".")