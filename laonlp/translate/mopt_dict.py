# -*- coding: utf-8 -*-
import csv
import os

from laonlp.corpus import mopt_dict

def dictionary(word: str, src: str, tarng: str):
    if src == "lao" and tarng == "eng":
        _temp = mopt_dict.get_lao_eng()
        if word not in list(_temp.keys()):
            return None
        return _temp[word]
    elif src == "eng" and tarng == "lao":
        _temp = mopt_dict.get_eng_lao()
        if word not in list(_temp.keys()):
            return None
        return _temp[word]
    else:
        return word