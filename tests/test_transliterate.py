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
        self.assertEqual(transliterate("ສະ", "moh2020")+transliterate("ບາຍ", "moh2020")+transliterate("ດີ", "moh2020"), "sabaydi")
        self.assertEqual(transliterate("ສະ", "moh2020")+transliterate("ຫວັນ", "moh2020")+transliterate("ນະ", "moh2020")+transliterate("ເຂດ", "moh2020"), "savannakhet")
        self.assertEqual(transliterate("ພາ", "moh2020")+transliterate("ສາ", "moh2020")+transliterate("ລາວ", "moh2020"), "phasalao")
        
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

    def test_transliterate_ipa(self):
        # Test IPA romanization with basic examples
        # "ສະບາຍດີ" (hello) should romanize to IPA
        self.assertIsNotNone(transliterate("ສະບາຍດີ", "ipa"))
        
    def test_transliterate_ipa_consonants(self):
        # Test IPA consonant mappings
        self.assertEqual(transliterate("ກ", "ipa"), "k")
        self.assertEqual(transliterate("ຂ", "ipa"), "kʰ")  # aspirated
        self.assertEqual(transliterate("ງ", "ipa"), "ŋ")   # velar nasal
        self.assertEqual(transliterate("ຈ", "ipa"), "tɕ")  # voiceless alveolo-palatal affricate
        self.assertEqual(transliterate("ດ", "ipa"), "d")
        self.assertEqual(transliterate("ຕ", "ipa"), "t")
        self.assertEqual(transliterate("ທ", "ipa"), "tʰ")  # aspirated
        self.assertEqual(transliterate("ນ", "ipa"), "n")
        self.assertEqual(transliterate("ບ", "ipa"), "b")
        self.assertEqual(transliterate("ປ", "ipa"), "p")
        self.assertEqual(transliterate("ຜ", "ipa"), "pʰ")  # aspirated
        self.assertEqual(transliterate("ຝ", "ipa"), "f")
        self.assertEqual(transliterate("ພ", "ipa"), "pʰ")  # aspirated
        self.assertEqual(transliterate("ມ", "ipa"), "m")
        self.assertEqual(transliterate("ຢ", "ipa"), "j")
        self.assertEqual(transliterate("ຍ", "ipa"), "ɲ")   # palatal nasal
        self.assertEqual(transliterate("ລ", "ipa"), "l")
        self.assertEqual(transliterate("ວ", "ipa"), "ʋ")   # labiodental approximant
        self.assertEqual(transliterate("ສ", "ipa"), "s")
        self.assertEqual(transliterate("ຫ", "ipa"), "h")
        self.assertEqual(transliterate("ອ", "ipa"), "ʔ")   # glottal stop
        self.assertEqual(transliterate("ຮ", "ipa"), "h")
        
    def test_transliterate_ipa_vowels(self):
        # Test IPA vowel mappings
        self.assertEqual(transliterate("ະ", "ipa"), "aʔ")  # short a with glottal stop
        self.assertEqual(transliterate("ັ", "ipa"), "a")
        self.assertEqual(transliterate("າ", "ipa"), "aː")  # long a
        self.assertEqual(transliterate("ິ", "ipa"), "i")
        self.assertEqual(transliterate("ີ", "ipa"), "iː")  # long i
        self.assertEqual(transliterate("ຶ", "ipa"), "ɯ")   # close central unrounded
        self.assertEqual(transliterate("ື", "ipa"), "ɯː")  # long ue
        self.assertEqual(transliterate("ຸ", "ipa"), "u")
        self.assertEqual(transliterate("ູ", "ipa"), "uː")  # long u
        self.assertEqual(transliterate("ເ", "ipa"), "eː")
        self.assertEqual(transliterate("ແ", "ipa"), "ɛː")  # open-mid front unrounded
        self.assertEqual(transliterate("ໂ", "ipa"), "oː")
        self.assertEqual(transliterate("ໃ", "ipa"), "aj")
        self.assertEqual(transliterate("ໄ", "ipa"), "aj")
        self.assertEqual(transliterate("ໍ", "ipa"), "ɔː")  # open-mid back rounded
        
    def test_transliterate_ipa_digits(self):
        # Test digit mappings in IPA (same as Arabic numerals)
        self.assertEqual(transliterate("໐໑໒໓໔໕໖໗໘໙", "ipa"), "0123456789")
        
    def test_transliterate_ipa_tone_marks(self):
        # Test that tone marks are removed in basic IPA
        self.assertEqual(transliterate("ກ່", "ipa"), "k")
        self.assertEqual(transliterate("ກ້", "ipa"), "k")
        self.assertEqual(transliterate("ກ໊", "ipa"), "k")
        self.assertEqual(transliterate("ກ໋", "ipa"), "k")
