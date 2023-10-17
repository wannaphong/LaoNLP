# -*- coding: utf-8 -*-

import unittest
from laonlp.translate import word_dictionary


class TestTagPackage(unittest.TestCase):
    def test_word_dictionary(self):
        self.assertNotEqual(word_dictionary("cat", "eng", "lao"), ["cat"])
        self.assertNotEqual(word_dictionary("ມັດ້າຣະ", "lao", "eng"), ["ມັດ້າຣະ"])
        self.assertEqual(word_dictionary("nonexistent_word", "eng", "lao"), [])
        self.assertEqual(word_dictionary("nonexistent_word", "lao", "eng"), [])
        self.assertEqual(word_dictionary("nonexistent_word", "test", "test"), ["nonexistent_word"])
