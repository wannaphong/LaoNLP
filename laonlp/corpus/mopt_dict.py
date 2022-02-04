# -*- coding: utf-8 -*-
import csv
import os

from laonlp.corpus import laonlp_path
from collections import defaultdict
from laonlp.corpus.core import get_path_corpus
corpus_path = get_path_corpus("lao-eng-dictionary.csv")
list_data=[]
with open(corpus_path,encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_data.append(row)


def get_lao_eng()->dict:
    _w = defaultdict(list)
    for i in list_data:
        _w[i['LaoWord']].append(i['English'])
    return _w


def get_eng_lao()->dict:
    _w = defaultdict(list)
    for i in list_data:
        _w[i['English']].append(i['LaoWord'])
    return _w


def get_pronunciation()->dict:
    _w = defaultdict(list)
    for i in list_data:
        _w[i['LaoWord']].append(i['Pronunciation'])
    return _w


def get_type()->dict:
    _w = defaultdict(list)
    for i in list_data:
        _w[i['LaoWord']].append(i['Type'])
    return _w
