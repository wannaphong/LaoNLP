# -*- coding: utf-8 -*-
"""
Copyright 2020 - 2024 Wannaphong Phatthiyaphaibun

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
__all__ = [
    "lao2thai_script",
    "thai2lao_script",
    "lao2thai_transliteration",
    "thai2lao_transliteration",
    "transliterate"
]

# Naive Lao script to Thai script transliteration.
# Data from https://github.com/google/language-resources/blob/master/lo/Laoo-Thai.txt
lao2thai_transliteration = {
    "\u0e81": "\u0e01",  # LAO LETTER KO KAY    → THAI CHARACTER KO KAI
    "\u0e82": "\u0e02",  # LAO LETTER KHO KHAY  → THAI CHARACTER KHO KHAI
    "\u0e84": "\u0e04",  # LAO LETTER KHO KHUAY → THAI CHARACTER KHO KHWAI
    "\u0e87": "\u0e07",  # LAO LETTER NGO NGU   → THAI CHARACTER NGO NGU
    "\u0e88": "\u0e08",  # LAO LETTER CO COK    → THAI CHARACTER CHO CHAN
    "\u0e8a": "\u0e0a",  # LAO LETTER SO SANG   → THAI CHARACTER CHO CHANG
    "\u0e8d": "\u0e0d",  # LAO LETTER NYO NYUNG → THAI CHARACTER YO YING
    "\u0e94": "\u0e14",  # LAO LETTER DO DEK    → THAI CHARACTER DO DEK
    "\u0e95": "\u0e15",  # LAO LETTER TO TA     → THAI CHARACTER TO TAO
    "\u0e96": "\u0e16",  # LAO LETTER THO THONG → THAI CHARACTER THO THUNG
    "\u0e97": "\u0e17",  # LAO LETTER THO THUNG → THAI CHARACTER THO THAHAN
    "\u0e99": "\u0e19",  # LAO LETTER NO NOK    → THAI CHARACTER NO NU
    "\u0e9a": "\u0e1a",  # LAO LETTER BO BE     → THAI CHARACTER BO BAIMAI
    "\u0e9b": "\u0e1b",  # LAO LETTER PO PA     → THAI CHARACTER PO PLA
    "\u0e9c": "\u0e1c",  # LAO LETTER PHO PHENG → THAI CHARACTER PHO PHUNG
    "\u0e9d": "\u0e1d",  # LAO LETTER FO FA     → THAI CHARACTER FO FA
    "\u0e9e": "\u0e1e",  # LAO LETTER PHO PHU   → THAI CHARACTER PHO PHAN
    "\u0e9f": "\u0e1f",  # LAO LETTER FO FAY    → THAI CHARACTER FO FAN
    "\u0ea1": "\u0e21",  # LAO LETTER MO MA     → THAI CHARACTER MO MA
    "\u0ea2": "\u0e22",  # LAO LETTER YO YA     → THAI CHARACTER YO YAK
    "\u0ea3": "\u0e23",  # LAO LETTER RO ROT    → THAI CHARACTER RO RUA
    "\u0ea5": "\u0e25",  # LAO LETTER LO LING   → THAI CHARACTER LO LING
    "\u0ea7": "\u0e27",  # LAO LETTER WO WI     → THAI CHARACTER WO WAEN
    "\u0eaa": "\u0e2a",  # LAO LETTER SO SYA    → THAI CHARACTER SO SUA
    "\u0eab": "\u0e2b",  # LAO LETTER HO HAY    → THAI CHARACTER HO HIP
    "\u0ead": "\u0e2d",  # LAO LETTER O O       → THAI CHARACTER O ANG
    "\u0eae": "\u0e2e",  # LAO LETTER HO HYA    → THAI CHARACTER HO NOKHUK
    "\u0eaf": "\u0e2f",  # LAO ELLIPSIS → THAI CHARACTER PAIYAN NOI
    "\u0eb0": "\u0e30",  # LAO VOWEL SIGN A       → THAI CHARACTER SARA A
    "\u0eb1": "\u0e31",  # LAO VOWEL SIGN MAI KAN → THAI CHARACTER MAI HAN-AKAT
    "\u0eb2": "\u0e32",  # LAO VOWEL SIGN AA      → THAI CHARACTER SARA AA
    "\u0eb3": "\u0e33",  # LAO VOWEL SIGN AM      → THAI CHARACTER SARA AM
    "\u0eb4": "\u0e34",  # LAO VOWEL SIGN I       → THAI CHARACTER SARA I
    "\u0eb5": "\u0e35",  # LAO VOWEL SIGN II      → THAI CHARACTER SARA II
    "\u0eb6": "\u0e36",  # LAO VOWEL SIGN Y       → THAI CHARACTER SARA UE
    "\u0eb7": "\u0e37",  # LAO VOWEL SIGN YY      → THAI CHARACTER SARA UEE
    "\u0eb8": "\u0e38",  # LAO VOWEL SIGN U       → THAI CHARACTER SARA U
    "\u0eb9": "\u0e39",  # LAO VOWEL SIGN UU      → THAI CHARACTER SARA UU
    "\u0ebb": "",        # LAO VOWEL SIGN MAI KONG", cf. Lao ເຈົ້າ vs. Thai เจ้า
    "\u0ebc": "\u0e25",  # LAO SEMIVOWEL SIGN LO        → THAI CHARACTER LO LING
    "\u0ebd": "\u0e0d",  # LAO SEMIVOWEL SIGN NYO FYANG → THAI CHARACTER YO YING
    "\u0ec0": "\u0e40",  # LAO VOWEL SIGN E           → THAI CHARACTER SARA E
    "\u0ec1": "\u0e41",  # LAO VOWEL SIGN EI          → THAI CHARACTER SARA AE
    "\u0ec2": "\u0e42",  # LAO VOWEL SIGN O           → THAI CHARACTER SARA O
    "\u0ec3": "\u0e43",  # LAO VOWEL SIGN AY MAI MUAN → THAI CHARACTER SARA AI MAI MUAN
    "\u0ec4": "\u0e44",  # LAO VOWEL SIGN AI MAI MAY  → THAI CHARACTER SARA AI MAI MALAI
    "\u0ec6": "\u0e46",  # LAO KO LA → THAI CHARACTER MAI YAMOK
    "\u0ec8": "\u0e48",  # LAO TONE MAI EK     → THAI CHARACTER MAI EK
    "\u0ec9": "\u0e49",  # LAO TONE MAI THO    → THAI CHARACTER MAI THO
    "\u0eca": "\u0e4a",  # LAO TONE MAI TI     → THAI CHARACTER MAI TRI
    "\u0ecb": "\u0e4b",  # LAO TONE MAI CATAWA → THAI CHARACTER MAI CHATTAWA
    "\u0ecc": "\u0e4c",  # LAO CANCELLATION MARK → THAI CHARACTER THANTHAKHAT
    "\u0ecd": "\u0e4d",  # LAO NIGGAHITA → THAI CHARACTER NIKHAHIT
    "\u0ed0": "\u0e50",  # LAO DIGIT ZERO  → THAI DIGIT ZERO
    "\u0ed1": "\u0e51",  # LAO DIGIT ONE   → THAI DIGIT ONE
    "\u0ed2": "\u0e52",  # LAO DIGIT TWO   → THAI DIGIT TWO
    "\u0ed3": "\u0e53",  # LAO DIGIT THREE → THAI DIGIT THREE
    "\u0ed4": "\u0e54",  # LAO DIGIT FOUR  → THAI DIGIT FOUR
    "\u0ed5": "\u0e55",  # LAO DIGIT FIVE  → THAI DIGIT FIVE
    "\u0ed6": "\u0e56",  # LAO DIGIT SIX   → THAI DIGIT SIX
    "\u0ed7": "\u0e57",  # LAO DIGIT SEVEN → THAI DIGIT SEVEN
    "\u0ed8": "\u0e58",  # LAO DIGIT EIGHT → THAI DIGIT EIGHT
    "\u0ed9": "\u0e59",  # LAO DIGIT NINE  → THAI DIGIT NINE
    "\u0edc": "\u0e2b\u0e19",  # LAO HO NO → HO HIP + NO NU
    "\u0edd": "\u0e2b\u0e21",  # LAO HO MO → HO HIP + MO MA
}
lao_char = list(lao2thai_transliteration.keys())
thai2lao_transliteration = dict((v, k) for k, v in lao2thai_transliteration.items())
thai_char = list(thai2lao_transliteration.keys())
# Lao transliteration to ASCII from AnyAscii (Line 3147-3230):
# https://github.com/anyascii/anyascii/blob/master/table.tsv
lao2ascii = str.maketrans({
    "ກ": "k",
    "ຂ": "kh",
    "ຄ": "kh",
    "ຆ": "gh",
    "ງ": "ng",
    "ຈ": "ch",
    "ຉ": "ch",
    "ຊ": "x",
    "ຌ": "jh",
    "ຍ": "gn",
    "ຎ": "n",
    "ຏ": "t",
    "ຐ": "th",
    "ຑ": "d",
    "ຒ": "dh",
    "ຓ": "n",
    "ດ": "d",
    "ຕ": "t",
    "ຖ": "th",
    "ທ": "th",
    "ຘ": "dh",
    "ນ": "n",
    "ບ": "b",
    "ປ": "p",
    "ຜ": "ph",
    "ຝ": "f",
    "ພ": "ph",
    "ຟ": "f",
    "ຠ": "bh",
    "ມ": "m",
    "ຢ": "y",
    "ຣ": "r",
    "ລ": "l",
    "ວ": "v",
    "ຨ": "s",
    "ຩ": "s",
    "ສ": "s",
    "ຫ": "h",
    "ຬ": "l",
    "ອ": "ອ",
    "ຮ": "h",
    "ຯ": "...",
    "ະ": "a",
    "ັ": "a",
    "າ": "a",
    "ຳ": "am",
    "ິ": "i",
    "ີ": "i",
    "ຶ": "u",
    "ື": "u",
    "ຸ": "ou",
    "ູ": "ou",
    "຺": "຺",
    "ົ": "o",
    "ຼ": "l",
    "ຽ": "y",
    "ເ": "e",
    "ແ": "e",
    "ໂ": "o",
    "ໃ": "ai",
    "ໄ": "ai",
    "ໆ": "-",
    "່": "່",
    "້": "້",
    "໊": "໊",
    "໋": "໋",
    "໌": "໌",
    "ໍ": "o",
    "໎": "໎",
    "໐": "0",
    "໑": "1",
    "໒": "2",
    "໓": "3",
    "໔": "4",
    "໕": "5",
    "໖": "6",
    "໗": "7",
    "໘": "8",
    "໙": "9",
    "ໜ": "n",
    "ໝ": "m",
    "ໞ": "g",
    "ໟ": "gn",
    "ༀ": "Om",
})


def lao2thai_script(text: str) -> str:
    """
    Lao to Thai script

    :param str sent: lao text
    :return: returns a string of thai script
    :rtype: str
    """
    new_text = ""
    for c in text:
        if c in lao_char:
            new_text += lao2thai_transliteration[c]
        else:
            new_text += c
    return new_text


def thai2lao_script(text: str) -> str:
    """
    Thai to Lao script

    :param str sent: thai text
    :return: returns a string of lao script
    :rtype: str
    """
    new_text = ""
    for c in text:
        if c in thai_char:
            new_text += thai2lao_transliteration[c]
        else:
            new_text += c
    return new_text


def transliterate(lao_word: str, engine: str = "anyascii") -> str:
    """
    Lao transliterate

    :param str sent: Lao text
    :param str engine: engine. Now, LaoNLP support anyascii only.
    :return: returns a Lao transliteration.
    :rtype: str
    """
    return lao_word.translate(lao2ascii)
