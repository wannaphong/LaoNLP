# -*- coding: utf-8 -*-
import os
from typing import List
from laonlp.corpus import laonlp_path
corpus_path = os.path.join(laonlp_path, "corpus")


def lao_dictionary() -> List[str]:
    path=os.path.join(corpus_path, "Lao-Dictionary.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lo_spellcheckdict() -> List[str]:
    path=os.path.join(corpus_path, "lo_spellcheck_dict.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lo_wannaphongdict() -> List[str]:
    path=os.path.join(corpus_path, "lao-wannaphong.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lo_wiktionarydict() -> List[str]:
    path=os.path.join(corpus_path, "wiktionary-20210720.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lao_words() -> List[str]:
    return list(set(lao_dictionary()+lo_spellcheckdict()+lo_wannaphongdict()+lo_wiktionarydict()))
