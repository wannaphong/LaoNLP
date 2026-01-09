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

# Ministry of Health 2020 Romanization System
# Based on the standardized romanization used in Lao health documentation
# Reference: https://laoconverter.info/moh2020.html
lao2moh2020 = str.maketrans({
    # Consonants
    "ກ": "k",      # KO
    "ຂ": "kh",     # KHO KHAI
    "ຄ": "kh",     # KHO KHUAI
    "ຆ": "kh",     # (rare)
    "ງ": "ng",     # NGO
    "ຈ": "ch",     # CHO
    "ຉ": "ch",     # (rare)
    "ຊ": "s",      # SO (palatalized)
    "ຌ": "ny",     # (rare)
    "ຍ": "y",      # NYO
    "ຎ": "d",      # (rare Sanskrit)
    "ຏ": "t",      # (rare Sanskrit)
    "ຐ": "th",     # (rare Sanskrit)
    "ຑ": "th",     # (rare Sanskrit)
    "ຒ": "th",     # (rare Sanskrit)
    "ຓ": "n",      # (rare Sanskrit)
    "ດ": "d",      # DO
    "ຕ": "t",      # TO
    "ຖ": "th",     # THO THUNG
    "ທ": "th",     # THO THONG
    "ຘ": "th",     # (rare)
    "ນ": "n",      # NO
    "ບ": "b",      # BO
    "ປ": "p",      # PO
    "ຜ": "ph",     # PHO PHUNG
    "ຝ": "f",      # FO FA
    "ພ": "ph",     # PHO PHEUNG
    "ຟ": "f",      # FO FAI
    "ຠ": "ph",     # (rare)
    "ມ": "m",      # MO
    "ຢ": "y",      # YO
    "ຣ": "r",      # RO
    "ລ": "l",      # LO
    "ວ": "v",      # VO/WO
    "ຨ": "s",      # (rare Sanskrit)
    "ຩ": "s",      # (rare Sanskrit)
    "ສ": "s",      # SO
    "ຫ": "h",      # HO
    "ຬ": "l",      # (rare Sanskrit)
    "ອ": "o",      # O
    "ຮ": "h",      # HO (final)
    # Vowels and vowel signs
    "ະ": "a",      # short A
    "ັ": "a",      # mai kan (short A above)
    "າ": "a",      # long AA
    "ຳ": "am",     # AM
    "ິ": "i",      # short I
    "ີ": "i",      # long II
    "ຶ": "ue",     # short UE
    "ື": "ue",     # long UEE
    "ຸ": "u",      # short U
    "ູ": "u",      # long UU
    "ົ": "o",      # mai kong
    "ຼ": "l",      # semivowel L
    "ຽ": "ia",     # IA
    "ເ": "e",      # E (before consonant)
    "ແ": "ae",     # AE (before consonant)
    "ໂ": "o",      # O (before consonant)
    "ໃ": "ai",     # AI
    "ໄ": "ai",     # AI (alternative)
    # Tone marks (omitted in romanization)
    "່": "",       # mai ek (tone 1)
    "້": "",       # mai tho (tone 2)
    "໊": "",       # mai ti (tone 3)
    "໋": "",       # mai chatawa (tone 4)
    # Other marks
    "໌": "",       # cancellation mark (thanthakhat)
    "ໍ": "o",      # mai noi
    "ໆ": "",       # repetition mark
    "ຯ": "...",    # ellipsis
    # Digits
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
    # Special combinations
    "ໜ": "n",     # HO NO
    "ໝ": "m",     # HO MO
})


def _apply_moh2020_rules(text: str, lao_text: str) -> str:
    """
    Apply MOH 2020-specific romanization rules.
    
    :param str text: Romanized text from character mapping
    :param str lao_text: Original Lao text
    :return: Text with MOH 2020 rules applied
    :rtype: str
    """
    import re
    
    # Rule 1: Silent ຫ (h) before certain consonants (w, y, l, r, n, m)
    # Must apply before vowel reordering
    # Special case: ຫວ (hv from mapping) stays 'v'
    # Other silent h cases
    text = re.sub(r'h([vylrnm])', r'\1', text)
    
    # Rule 2: Final consonant changes (before vowel reordering)
    # 'd' at end -> 't' (only when part of a multi-character syllable)
    text = re.sub(r'(?<=.)d\b', 't', text)
    text = re.sub(r'(?<=.)d(?=\s)', 't', text)
    
    # Rule 3: 'v' at true end of word -> 'o'
    # "lav" -> "lao", but "van" stays "van" unless at word end
    text = re.sub(r'(?<=.)v\b', 'o', text)
    
    # Rule 4: Reorder vowel 'e' that comes before consonants
    # In Lao, ເ appears before the consonant, but romanizes after it
    # Pattern: e + consonant_cluster -> consonant_cluster + e
    # Only apply when 'e' is truly misplaced (at start of word/text)
    # "ekht" -> "khet", but don't change "khet" 
    
    # Use word boundary: \b ensures we're at the start of a word
    # Match: word_boundary + e + consonants + more_consonants
    text = re.sub(r'\be([bcdghklmnprsty]{1,2})([bcdghklmnprsty])', r'\1e\2', text)
    # Match: word_boundary + e + consonants + (end)
    text = re.sub(r'\be([bcdghklmnprsty]{1,2})\b', r'\1e', text)
    
    return text


def lao2thai_script(text: str) -> str:
    """
    Lao to Thai script

    :param str sent: lao text
    :return: returns a string of thai script
    :rtype: str

    :Example:
    ::

        from laonlp.transliterate import *

        print(lao2thai_script("ແມວ")) # แมว
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

    :Example:
    ::

        from laonlp.transliterate import *

        print(thai2lao_script("แมว")) # ແມວ
    """
    new_text = ""
    for c in text:
        if c in thai_char:
            new_text += thai2lao_transliteration[c]
        else:
            new_text += c
    return new_text


# IPA (International Phonetic Alphabet) Romanization
# Based on Lingua::LO::NLP::Romanize::IPA
# Reference: https://github.com/mbethke/Lingua-LO-NLP
lao2ipa = str.maketrans({
    # Consonants
    "ກ": "k",       # KO
    "ຂ": "kʰ",      # KHO KHAI (aspirated)
    "ຄ": "kʰ",      # KHO KHUAI (aspirated)
    "ງ": "ŋ",       # NGO (velar nasal)
    "ຈ": "tɕ",      # CHO (voiceless alveolo-palatal affricate)
    "ຊ": "s",       # SO (sibilant)
    "ສ": "s",       # SO
    "ຍ": "ɲ",       # NYO (palatal nasal)
    "ດ": "d",       # DO (becomes 't' in final position)
    "ຕ": "t",       # TO
    "ຖ": "tʰ",      # THO THUNG (aspirated)
    "ທ": "tʰ",      # THO THONG (aspirated)
    "ນ": "n",       # NO
    "ບ": "b",       # BO (becomes 'p' in final position)
    "ປ": "p",       # PO
    "ຜ": "pʰ",      # PHO PHUNG (aspirated)
    "ຝ": "f",       # FO FA
    "ພ": "pʰ",      # PHO PHEUNG (aspirated)
    "ຟ": "f",       # FO FAI
    "ມ": "m",       # MO
    "ຢ": "j",       # YO
    "ຣ": "r",       # RO
    "ລ": "l",       # LO
    "ວ": "ʋ",       # VO/WO (labiodental approximant)
    "ຫ": "h",       # HO
    "ອ": "ʔ",       # O (glottal stop)
    "ຮ": "h",       # HO (final)
    # Vowels and vowel signs
    "ະ": "aʔ",      # short A with glottal stop
    "ັ": "a",       # mai kan (short A)
    "າ": "aː",      # long AA (length marker)
    "ຳ": "am",      # AM
    "ິ": "i",       # short I
    "ີ": "iː",      # long II
    "ຶ": "ɯ",       # short UE (close central unrounded)
    "ື": "ɯː",      # long UEE
    "ຸ": "u",       # short U
    "ູ": "uː",      # long UU
    "ົ": "o",       # mai kong
    "ຼ": "l",       # semivowel L
    "ຽ": "iːə",     # IA (diphthong)
    "ເ": "eː",      # E (before consonant)
    "ແ": "ɛː",      # AE (open-mid front unrounded)
    "ໂ": "oː",      # O (before consonant)
    "ໃ": "aj",      # AI
    "ໄ": "aj",      # AI (alternative)
    # Tone marks (preserved in IPA for tonal information)
    "່": "",        # mai ek (tone 1) - omitted in basic IPA
    "້": "",        # mai tho (tone 2) - omitted in basic IPA
    "໊": "",        # mai ti (tone 3) - omitted in basic IPA
    "໋": "",        # mai chatawa (tone 4) - omitted in basic IPA
    # Other marks
    "໌": "",        # cancellation mark
    "ໍ": "ɔː",      # mai noi (open-mid back rounded with length)
    "ໆ": "",        # repetition mark
    "ຯ": "...",     # ellipsis
    # Digits
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
    # Special combinations
    "ໜ": "n",      # HO NO
    "ໝ": "m",      # HO MO
})


def transliterate(lao_word: str, engine: str = "anyascii") -> str:
    """
    Lao transliterate

    :param str lao_word: Lao text
    :param str engine: engine. Supported engines: 'anyascii', 'moh2020', 'ipa'
    :return: returns a Lao transliteration.
    :rtype: str
    """
    if engine == "moh2020":
        result = lao_word.translate(lao2moh2020)
        return _apply_moh2020_rules(result, lao_word)
    elif engine == "ipa":
        return lao_word.translate(lao2ipa)
    return lao_word.translate(lao2ascii)
