# -*- coding: utf-8 -*-

import unittest
from laonlp.corpus.core import get_path_corpus
from laonlp.corpus.lao_words import lao_dictionary, lao_spellcheckdict, lao_wannaphongdict, lao_wiktionarydict, lao_words, lao_stopwords
from laonlp.corpus.mopt_dict import get_lao_eng, get_eng_lao, get_pronunciation, get_type


class TestCorpusPackage(unittest.TestCase):
    def test_get_path_corpus(self):
        self.assertIsNotNone(get_path_corpus('test'))

    def test_lao_dictionary(self):
        self.assertIsNotNone(lao_dictionary())

    def test_lao_spellcheckdict(self):
        self.assertIsNotNone(lao_spellcheckdict())

    def test_lao_wannaphongdict(self):
        self.assertIsNotNone(lao_wannaphongdict())

    def test_lao_wiktionarydict(self):
        self.assertIsNotNone(lao_wiktionarydict())

    def test_lao_words(self):
        self.assertIsNotNone(lao_words())

    def test_lao_stopwords(self):
        self.assertIsNotNone(lao_stopwords())

    def test_get_lao_eng(self):
        self.assertIsNotNone(get_lao_eng())

    def test_get_eng_lao(self):
        self.assertIsNotNone(get_eng_lao())

    def test_get_pronunciation(self):
        self.assertIsNotNone(get_pronunciation())

    def test_get_type(self):
        self.assertIsNotNone(get_type())
