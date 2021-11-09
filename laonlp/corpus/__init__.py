# -*- coding: utf-8 -*-
import laonlp
import os

laonlp_path = os.path.dirname(laonlp.__file__)

from laonlp.corpus.lao_words import *
from laonlp.corpus.core import get_path_corpus

__all__ = [
    "lao_dictionary",
    "lao_spellcheckdict",
    "lao_words",
    "lao_wannaphongdict",
    "lao_wiktionarydict",
    "get_path_corpus",
    "lao_stopwords"
]