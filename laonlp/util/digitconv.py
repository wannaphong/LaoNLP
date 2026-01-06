# -*- coding: utf-8 -*-
"""
Copyright 2020 - 2026 Wannaphong Phatthiyaphaibun

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
_places = [
    "", "ສິບ", "ຮ້ອຍ", "ພັນ", "ຫມື່ນ", "ແສນ", "ລ້ານ", "ຕື້",
]
_exceptions = {"ຫມື່ນ": "ສິບ", "ນຶ່ງສິບ": "ສິບ", "ສອງສິບນຶ່ງ": "ຊາວເອັດ", "ສອງສິບ": "ຊາວ", "ສິບນຶ່ງ": "ສິບເອັດ"}

_dict_lao_arabic = dict(zip(list(NUMBERS), list(_arabic_numerals)))
_dict_arabic_lao = dict(zip(list(_arabic_numerals), list(NUMBERS)))
_lao_arabic_table = str.maketrans(_dict_lao_arabic)
_arabic_lao_table = str.maketrans(_dict_arabic_lao)


def lao_digit_to_arabic_digit(text: str) -> str:
    """
    Lao digit to Arabic digit

    :param str text: Lao digit text
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


def num_to_laoword(number: int):
    """
    Number to Lao word

    :param number int: Integer to be converted
    :return: returns a string of Lao word representation of the integer
    :rtype: str
    """
    output = ""
    prefix = ""

    if number is None:
        return ""

    if number == 0:
        return _pronunciation[-1]

    sign = number < 0
    number = str(abs(number))

    # Special case > 1e9
    if len(number) >= 10:
        prefix = num_to_laoword(int(number[:-9])) + _places[-1]
        number = number[-9:]

    prev_value = ""

    for place, value in enumerate(list(number[::-1])):
        if place % 6 == 0 and place > 0:
            output = _places[6] + output

        if value != "0":
            output = _pronunciation[int(value) - 1] + _places[place % 6] + output

        # Special place exception
        if place % 6 == 3 and prev_value == "0":
            output = _places[3] + output

        prev_value = value

    for search, replac in _exceptions.items():
        output = output.replace(search, replac)

    if sign:
        output = "ລົບ" + output

    return prefix + output
