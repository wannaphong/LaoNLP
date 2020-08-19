# -*- coding: utf-8 -*-
import os
from laonlp.corpus import laonlp_path
corpus_path = os.path.join(laonlp_path, "corpus")

def lao_dictionary()->list:
    path=os.path.join(corpus_path, "Lao-Dictionary.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]

def lo_spellcheckdict()->list:
    path=os.path.join(corpus_path, "lo_spellcheck_dict.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]

def lao_words()->list:
    return list(set(lao_dictionary()+lo_spellcheckdict()))
