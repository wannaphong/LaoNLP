# -*- coding: utf-8 -*-

import unittest
from laonlp.transliterate import lao2thai_script, thai2lao_script, transliterate


class TestTransliteratePackage(unittest.TestCase):
    def test_lao2thai_script(self):
        self.assertIsNotNone(lao2thai_script("ພາສາລາວໃນປັດຈຸບັນ."))

    def test_thai2lao_script(self):
        self.assertIsNotNone(thai2lao_script("พาสาลาว."))

    def test_transliterate(self):
        self.assertEqual(transliterate("ສະຫວັນນະເຂດ"), "sahvannaekhd")
    
    def test_transliterate_moh2020(self):
        # Test MOH 2020 romanization system
        self.assertEqual(transliterate("ສະບາຍດີ", "moh2020"), "sabanydi")
        self.assertEqual(transliterate("ສະຫວັນນະເຂດ", "moh2020"), "sahvannaekhd")
        self.assertEqual(transliterate("ພາສາລາວ", "moh2020"), "phasalav")
        
    def test_transliterate_moh2020_consonants(self):
        # Test consonant mappings
        self.assertEqual(transliterate("ກ", "moh2020"), "k")
        self.assertEqual(transliterate("ຂ", "moh2020"), "kh")
        self.assertEqual(transliterate("ງ", "moh2020"), "ng")
        self.assertEqual(transliterate("ຈ", "moh2020"), "ch")
        self.assertEqual(transliterate("ດ", "moh2020"), "d")
        self.assertEqual(transliterate("ຕ", "moh2020"), "t")
        self.assertEqual(transliterate("ນ", "moh2020"), "n")
        self.assertEqual(transliterate("ບ", "moh2020"), "b")
        self.assertEqual(transliterate("ປ", "moh2020"), "p")
        self.assertEqual(transliterate("ຜ", "moh2020"), "ph")
        self.assertEqual(transliterate("ຝ", "moh2020"), "f")
        self.assertEqual(transliterate("ພ", "moh2020"), "ph")
        self.assertEqual(transliterate("ມ", "moh2020"), "m")
        self.assertEqual(transliterate("ຢ", "moh2020"), "y")
        self.assertEqual(transliterate("ລ", "moh2020"), "l")
        self.assertEqual(transliterate("ວ", "moh2020"), "v")
        self.assertEqual(transliterate("ສ", "moh2020"), "s")
        self.assertEqual(transliterate("ຫ", "moh2020"), "h")
        self.assertEqual(transliterate("ຮ", "moh2020"), "h")
        
    def test_transliterate_moh2020_vowels(self):
        # Test vowel mappings
        self.assertEqual(transliterate("ະ", "moh2020"), "a")
        self.assertEqual(transliterate("າ", "moh2020"), "a")
        self.assertEqual(transliterate("ິ", "moh2020"), "i")
        self.assertEqual(transliterate("ີ", "moh2020"), "i")
        self.assertEqual(transliterate("ຶ", "moh2020"), "ue")
        self.assertEqual(transliterate("ື", "moh2020"), "ue")
        self.assertEqual(transliterate("ຸ", "moh2020"), "u")
        self.assertEqual(transliterate("ູ", "moh2020"), "u")
        self.assertEqual(transliterate("ເ", "moh2020"), "e")
        self.assertEqual(transliterate("ແ", "moh2020"), "ae")
        self.assertEqual(transliterate("ໂ", "moh2020"), "o")
        self.assertEqual(transliterate("ໃ", "moh2020"), "ai")
        self.assertEqual(transliterate("ໄ", "moh2020"), "ai")
        
    def test_transliterate_moh2020_digits(self):
        # Test digit mappings
        self.assertEqual(transliterate("໐໑໒໓໔໕໖໗໘໙", "moh2020"), "0123456789")
        
    def test_transliterate_moh2020_tone_marks(self):
        # Test that tone marks are removed (empty string)
        self.assertEqual(transliterate("ກ່", "moh2020"), "k")
        self.assertEqual(transliterate("ກ້", "moh2020"), "k")
        self.assertEqual(transliterate("ກ໊", "moh2020"), "k")
        self.assertEqual(transliterate("ກ໋", "moh2020"), "k")
