# -*- coding: utf-8 -*-
"""
Copyright 2020 - 2023 Wannaphong Phatthiyaphaibun

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import csv
from collections import defaultdict

from laonlp.corpus import laonlp_path
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
