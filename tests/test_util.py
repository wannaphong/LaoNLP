# -*- coding: utf-8 -*-

import unittest
from laonlp.util import (
    lao_digit_to_arabic_digit,
    arabic_digit_to_lao_digit,
    remove_tone_mark,
    num_to_laoword,
)


class TestTagPackage(unittest.TestCase):
    def test_lao_digit_to_arabic_digit(self):
        self.assertEqual(
            lao_digit_to_arabic_digit("໑໒໓໔໕໖໗໘໙໐"),
            "1234567890"
        )

    def test_arabic_digit_to_lao_digit(self):
        self.assertEqual(
            arabic_digit_to_lao_digit("1234567890"),
            "໑໒໓໔໕໖໗໘໙໐"
        )

    def test_remove_tone_mark(self):
        self.assertEqual(
            remove_tone_mark("ຜູ້"),
            "ຜູ"
        )

    def test_num_to_laoword(self):
        self.assertEqual(num_to_laoword(None), "")
        self.assertEqual(num_to_laoword(0), "ສູນ")
        self.assertEqual(num_to_laoword(112), "ນຶ່ງຮ້ອຍສິບສອງ")
        self.assertEqual(num_to_laoword(-273), "ລົບສອງຮ້ອຍເຈັດສິບສາມ")
        self.assertEqual(num_to_laoword(12101), "ສິບສອງພັນນຶ່ງຮ້ອຍນຶ່ງ")
        self.assertEqual(num_to_laoword(20000), "ຊາວພັນ")
        self.assertEqual(num_to_laoword(987654321), "ເກົ້າຮ້ອຍແປດສິບເຈັດລ້ານຫົກແສນຫ້າສິບສີ່ພັນສາມຮ້ອຍຊາວເອັດ")
        self.assertEqual(num_to_laoword(11987654321), "ສິບເອັດຕື້ເກົ້າຮ້ອຍແປດສິບເຈັດລ້ານຫົກແສນຫ້າສິບສີ່ພັນສາມຮ້ອຍຊາວເອັດ")
