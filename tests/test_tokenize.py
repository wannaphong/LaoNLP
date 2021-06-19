# -*- coding: utf-8 -*-

import unittest
from laonlp.tokenize import word_tokenize, sent_tokenize

class TestTokenizePackage(unittest.TestCase):
    def test_word_tokenize(self):
        self.assertIsNotNone(word_tokenize("ພາສາລາວໃນປັດຈຸບັນ."))

    def test_sent_tokenize(self):
        self.assertIsNotNone(sent_tokenize("ພາສາລາວໃນປັດຈຸບັນ.ນະຄອນຫຼວງວຽງຈັນ"))
