# -*- coding: utf-8 -*-

import unittest
from laonlp.util import *


class TestTagPackage(unittest.TestCase):
    def test_lao_digit_to_arabic_digit(self):
        self.assertEqual(
            lao_digit_to_arabic_digit("໑໒໓໔໕໖໗໘໙໐"),
            '1234567890'
        )
    def test_arabic_digit_to_lao_digit(self):
        self.assertEqual(
            arabic_digit_to_lao_digit('1234567890'),
            "໑໒໓໔໕໖໗໘໙໐"
        )
    def test_remove_tone_mark(self):
        self.assertEqual(
            remove_tone_mark("ຜູ້"),
            'ຜູ'
        )