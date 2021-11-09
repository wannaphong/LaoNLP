# -*- coding: utf-8 -*-
import os
from typing import List
from typing import FrozenSet
from laonlp.corpus.core import get_path_corpus


def lao_dictionary() -> List[str]:
    path = get_path_corpus("Lao-Dictionary.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lao_spellcheckdict() -> List[str]:
    path = get_path_corpus("lo_spellcheck_dict.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lao_wannaphongdict() -> List[str]:
    path = get_path_corpus("lao-wannaphong.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lao_wiktionarydict() -> List[str]:
    path = get_path_corpus("wiktionary-20210720.txt")
    with open(path, "r", encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines() if i[0]!="#"]


def lao_words() -> List[str]:
    return list(set(lao_dictionary()+lao_spellcheckdict()+lao_wannaphongdict()+lao_wiktionarydict()))


def lao_stopwords() -> FrozenSet[str]:
    """
    Lao stopword list

    Return a frozenset of Lao stopwords

    :return: :class:`frozenset` containing stopwords.
    :rtype: :class:`frozenset`
    """
    path = get_path_corpus("stopwords_lao.txt")
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()
    lines = [line.strip() for line in lines if line.startswith("#") == False]
    return frozenset(filter(None, lines))
