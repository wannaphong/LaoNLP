# -*- coding: utf-8 -*-

import unittest
from laonlp.transliterate import lao2thai_script, thai2lao_script, transliterate


class TestTransliteratePackage(unittest.TestCase):
    def test_lao2thai_script(self):
        self.assertIsNotNone(lao2thai_script("ພາສາລາວໃນປັດຈຸບັນ."))

    def test_thai2lao_script(self):
        self.assertIsNotNone(thai2lao_script("พาสาลาว"))

    def test_transliterate(self):
        self.assertEquals(transliterate("ສະຫວັນນະເຂດ"),"sahvannaekhd")
