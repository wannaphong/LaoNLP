# -*- coding: utf-8 -*-
NUMBERS = "໑໒໓໔໕໖໗໘໙໐"
_arabic_numerals = "1234567890"
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