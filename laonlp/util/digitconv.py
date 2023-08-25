# -*- coding: utf-8 -*-
"""
Copyright 2020 - 2023 Wannaphong Phatthiyaphaibun

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
NUMBERS = "໑໒໓໔໕໖໗໘໙໐"
_arabic_numerals = "1234567890"
_pronunciation = [
    "ນຶ່ງ",
    "ສອງ",
    "ສາມ",
    "ສີ່",
    "ຫ້າ",
    "ຫົກ",
    "ເຈັດ",
    "ແປດ",
    "ເກົ້າ",
    "ສູນ"
]
_dict_lao_arabic = {
    i:j for i,j in zip(list(NUMBERS), list(_arabic_numerals))
}
_dict_arabic_lao = {
    i:j for i,j in zip(list(_arabic_numerals), list(NUMBERS))
}
_lao_arabic_table = str.maketrans(_dict_lao_arabic)
_arabic_lao_table = str.maketrans(_dict_arabic_lao)


def lao_digit_to_arabic_digit(text: str) -> str:
    """
    Lao digit to Arabic digit

    :param str text: lao digit text
    :return: returns a string of Arabic digit
    :rtype: str
    """
    return text.translate(_lao_arabic_table)

def arabic_digit_to_lao_digit(text: str) -> str:
    """
    Arabic digit to Lao digit

    :param str text: Arabic digit text
    :return: returns a string of Lao digit
    :rtype: str
    """
    return text.translate(_arabic_lao_table)

def number2lao(numbers: int):
    """
    Numbers to La opronunciation
    """
    # TODO
    return ""
