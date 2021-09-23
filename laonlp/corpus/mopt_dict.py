# -*- coding: utf-8 -*-
import csv
import os

from laonlp.corpus import laonlp_path
corpus_path = os.path.join(laonlp_path, "corpus", "lao-eng-dictionary.csv")
list_data=[]
with open(corpus_path,encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_data.append(row)


def get_lao_eng():
    _w = {}
    for i in list_data:
        _w[i['LaoWord']] = i['English']
    return _w


def get_eng_lao():
    _w = {}
    for i in list_data:
        _w[i['English']] = i['LaoWord']
    return _w


def get_pronunciation():
    _w = {}
    for i in list_data:
        _w[i['LaoWord']] = i['Pronunciation']
    return _w


def get_type():
    _w = {}
    for i in list_data:
        _w[i['LaoWord']] = i['Type']
    return _w
