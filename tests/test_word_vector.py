# -*- coding: utf-8 -*-

import unittest
from laonlp.word_vector import Word2Vec


class TestTagPackage(unittest.TestCase):
    def test_word2vec(self):
        self.assertRaises(NotImplementedError, Word2Vec, model="cbow", corpus="unsupported_corpus")
        _m0 = Word2Vec(model="cbow")
        self.assertRaises(NotImplementedError, _m0.load_model, model="unsupported_model")
        self.assertIsNotNone(_m0.get_model())
        self.assertIsNotNone(_m0.doesnt_match(['test']))
        self.assertIsNotNone(_m0.most_similar_cosmul(['test'], ['test']))
        _m1 = Word2Vec(model="cbow")
        self.assertIsNotNone(_m1.similarity("ແປດ", "ແພະ"))
        _m2 = Word2Vec(model="skip-gram")
        self.assertIsNotNone(_m2.similarity("ແປດ", "ແພະ"))
