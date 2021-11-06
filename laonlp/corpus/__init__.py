# -*- coding: utf-8 -*-
import laonlp
import os

laonlp_path = os.path.dirname(laonlp.__file__)

from laonlp.corpus.lao_words import *
from laonlp.corpus.core import get_path_corpus

__all__ = [
    "lao_dictionary",
    "lo_spellcheckdict",
    "lao_words",
    "get_path_corpus"
]