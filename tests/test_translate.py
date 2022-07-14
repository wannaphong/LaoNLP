# -*- coding: utf-8 -*-

import unittest
from laonlp.translate import word_dictionary


class TestTagPackage(unittest.TestCase):
    def test_word_dictionary(self):
        self.assertIsNotNone(word_dictionary("cat","en","lao"))