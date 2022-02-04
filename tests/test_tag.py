# -*- coding: utf-8 -*-

import unittest
from laonlp.tokenize import word_tokenize
from laonlp.tag import pos_tag


class TestTagPackage(unittest.TestCase):
    def test_pos_tag(self):
        self.assertIsNotNone(pos_tag(word_tokenize("ພາສາລາວໃນປັດຈຸບັນ.")))
        self.assertIsNotNone(pos_tag(word_tokenize("ພາສາລາວໃນປັດຈຸບັນ."), corpus="SeqLabeling"))
        self.assertIsNotNone(pos_tag(word_tokenize("ພາສາລາວໃນປັດຈຸບັນ."), corpus="yunshan_cup_2020"))
