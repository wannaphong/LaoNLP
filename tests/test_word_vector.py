# -*- coding: utf-8 -*-

import unittest
from laonlp.word_vector import Word2Vec


class TestTagPackage(unittest.TestCase):
    def test_word2vec(self):
        _m1 = Word2Vec(model="cbow")
        self.assertIsNotNone(_m1.similarity("ແປດ","ແພະ"))
        _m2 = Word2Vec(model="skip-gram")
        self.assertIsNotNone(_m2.similarity("ແປດ","ແພະ"))