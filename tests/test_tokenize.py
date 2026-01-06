# -*- coding: utf-8 -*-

import unittest
from laonlp.tokenize import word_tokenize, sent_tokenize, syllable_tokenize


class TestTokenizePackage(unittest.TestCase):
    def test_word_tokenize(self):
        self.assertIsNotNone(word_tokenize("ພາສາລາວໃນປັດຈຸບັນ."))

    def test_sent_tokenize(self):
        self.assertEqual(
            sent_tokenize("ພາສາລາວໃນປັດຈຸບັນ.ນະຄອນຫຼວງວຽງຈັນ"),
            ["ພາສາລາວໃນປັດຈຸບັນ.", "ນະຄອນຫຼວງວຽງຈັນ"]
        )

    def test_syllable_tokenize(self):
        # Test basic syllable splitting
        self.assertEqual(
            syllable_tokenize("ສະບາຍດີ"),
            ["ສະ", "ບາຍ", "ດີ"]
        )
        
        # Test empty string
        self.assertEqual(
            syllable_tokenize(""),
            []
        )
        
        # Test more complex text
        self.assertEqual(
            syllable_tokenize("ພາສາລາວໃນປັດຈຸບັນ"),
            ["ພາ", "ສາ", "ລາວ", "ໃນ", "ປັດ", "ຈຸ", "ບັນ"]
        )
        
        # Test text with various syllable patterns
        self.assertEqual(
            syllable_tokenize("ກວ່າດອກ"),
            ["ກວ່າ", "ດອກ"]
        )
        
        self.assertEqual(
            syllable_tokenize("ເພື່ອນ"),
            ["ເພື່ອນ"]
        )
        
        # Test with Lao digits
        result = syllable_tokenize("ກວ່າດອກ໐໑໒໓")
        self.assertTrue(len(result) >= 2)
        self.assertEqual(result[0], "ກວ່າ")
        self.assertEqual(result[1], "ດອກ")
        
        # Test composed and decomposed sala am
        self.assertEqual(
            syllable_tokenize("ຄຳດີ"),
            ["ຄຳ", "ດີ"]
        )
        
        # Test more syllables
        self.assertEqual(
            syllable_tokenize("ກັນ"),
            ["ກັນ"]
        )
        
        self.assertEqual(
            syllable_tokenize("ກັວນ"),
            ["ກັວນ"]
        )
        
        self.assertEqual(
            syllable_tokenize("ກົດ"),
            ["ກົດ"]
        )
        
        self.assertEqual(
            syllable_tokenize("ແປຽ"),
            ["ແປຽ"]
        )
        
        self.assertEqual(
            syllable_tokenize("ມື້ນີ້"),
            ["ມື້", "ນີ້"]
        )
