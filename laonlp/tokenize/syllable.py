# -*- coding: utf-8 -*-
"""
Copyright 2020 - 2025 Wannaphong Phatthiyaphaibun

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
import re
from typing import List
from unicodedata import normalize as unicode_normalize


# Character classes based on Lao Unicode blocks
TONE_MARKS = "\u0EC8\u0EC9\u0ECA\u0ECB"  # LAO TONE MAI EK, THO, TI, CATAWA
CONSONANTS = "ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮໜໝ"
VOWELS_COMBINING = "\u0EB1\u0EB4\u0EB5\u0EB6\u0EB7\u0EB8\u0EB9\u0EBB\u0ECD"
VOWELS = "\u0EB0\u0EB1\u0EB2\u0EB3\u0EB4\u0EB5\u0EB6\u0EB7\u0EB8\u0EB9\u0EBB\u0EBC\u0EBD\u0EC0\u0EC1\u0EC2\u0EC3\u0EC4\u0ECD"

# Regular expression fragments based on PHISSAMAY et al:
# "Syllabification of Lao Script for Line Breaking"

# x0 - Leading vowels
x0_1 = "ເ"  # VOWEL SIGN E
x0_2 = "ແ"  # VOWEL SIGN EI
x0_3 = "ໂ"  # VOWEL SIGN O
x0_4 = "ໄ"  # VOWEL SIGN AI
x0_5 = "ໃ"  # VOWEL SIGN AY

x1 = "ຫ"  # HO SUNG (for forming aspirated consonants)
x = f"[{CONSONANTS}]"  # Core consonant
x2 = "[\u0EBC\u0EA3\u0EA7\u0EA5]"  # Semivowels: LO, RO, WO, LO
x3 = "[\u0EB8\u0EB9]"  # VOWEL SIGN U, UU
x4_12 = "[\u0EB4\u0EB5]"  # VOWEL SIGN I, II
x4_34 = "[\u0EB6\u0EB7]"  # VOWEL SIGN Y, YY
x4_5 = "\u0ECD"  # NIGGAHITA
x4_6 = "\u0EBB"  # VOWEL SIGN MAI KON
x4_7 = "\u0EB1"  # VOWEL SIGN MAI KAN
x4_1t4 = "[\u0EB4\u0EB5\u0EB6\u0EB7]"  # I, II, Y, YY

x5 = f"[{TONE_MARKS}]"  # Tone marks

x6_1 = "ວ"  # WO
x6_2 = "ອ"  # O
x6_3 = "ຽ"  # VOWEL SIGN NYOY
x6 = "[ວອຽ]"

x7_1 = "ະ"  # VOWEL SIGN A
x7_2 = "າ"  # VOWEL SIGN AA
x7_3 = "\u0EB3"  # VOWEL SIGN AM

x8_3t8 = "[ຍດນມຢບ]"  # End consonants (subset)
x8 = "[ກງຍດນມຢບວ]"  # End consonants (full)

x9 = "[ຈສຊພຟລ]"  # Foreign end consonants
x10_12 = "[ຯໆ]"  # Repetition marks
x10_3 = "\u0ECC"  # CANCELLATION MARK

x9a10_3 = f"(?:{x9}{x10_3})"  # Foreign consonant with cancellation mark

# Syllable pattern components following the original algorithm
re1_all = f"{x0_1}{x1}?{x}{x2}?"
re1_1 = f"{x5}?{x8}?{x9a10_3}?"
re1_2 = f"{x4_12}{x5}?{x8}?{x9a10_3}?"
re1_3 = f"{x4_34}{x5}?{x6_2}{x8}?{x9a10_3}?"
re1_4 = f"{x7_2}?{x7_1}"
re1_5 = f"{x4_6}{x5}?{x7_2}"
re1_6 = f"{x4_7}{x5}?{x8}{x9a10_3}?"
re1_8 = f"{x4_7}?{x5}?{x6_3}"

re2_all = f"{x0_2}{x1}?{x}{x2}?"
re2_1 = f"{x5}?{x6}?{x8}?{x9a10_3}?"
re2_2 = f"{x7_1}"
re2_3 = f"{x4_7}{x5}?{x8}{x9a10_3}?"

re3_all = f"{x0_3}{x1}?{x}{x2}?"
re3_1 = f"{x5}?{x8}?{x9a10_3}?"
re3_2 = f"{x7_1}"
re3_3 = f"{x4_7}{x5}?{x8_3t8}?"

re4 = f"{x0_4}{x1}?{x}{x2}?{x5}?{x6_1}?{x9a10_3}?"
re5 = f"{x0_5}{x1}?{x}{x2}?{x5}?{x6_1}?"

re6 = f"{x1}?{x}{x2}?{x3}{x5}?{x8}?{x9a10_3}?"
re7 = f"{x1}?{x}{x2}?{x4_1t4}{x5}?{x8}?{x9a10_3}?"
re8 = f"{x1}?{x}{x2}?{x4_5}{x5}?{x7_2}?{x9a10_3}?"
re9 = f"{x1}?{x}{x2}?{x4_6}{x5}?(?:{x8}{x9a10_3}?|{x6_1}{x7_1})"
re10 = f"{x1}?{x}{x2}?{x4_7}{x5}?{x6_1}?{x8}{x9a10_3}?"
re11 = f"{x1}?{x}{x2}?{x5}?{x6}{x8}{x9a10_3}?"
re12 = f"{x1}?{x}{x2}?{x5}?{x7_1}"
re13 = f"{x1}?{x}{x2}?{x5}?{x7_2}{x8}?{x9a10_3}?"
re14 = f"{x1}?{x}{x2}?{x5}?{x7_3}{x9a10_3}?"

re_num = "[໐໑໒໓໔໕໖໗໘໙]"  # Lao digits
rex1012 = f"{x10_12}"

# Build the basic syllable pattern
_re_basic_parts = [
    f"(?:{re1_all}(?:{re1_1}|{re1_2}|{re1_3}|{re1_4}|{re1_5}|{re1_6}|{re1_8}))",
    f"(?:{re2_all}(?:{re2_1}|{re2_2}|{re2_3}))",
    f"(?:{re3_all}(?:{re3_1}|{re3_2}|{re3_3}))",
    re4, re5, re6, re7, re8, re9, re10, re11, re12, re13, re14
]

_re_basic = f"(?:(?:(?:{'|'.join(_re_basic_parts)}){rex1012}?)|{re_num}+)"

# Lookahead for syllable boundaries
_re_lookahead_parts = [re6, re7, re8, re9, re10, re11, re12, re13, re14, f"{re_num}+"]
_re_lookahead = f"(?:{'|'.join(_re_lookahead_parts)})"

# Full syllable pattern with lookahead for proper boundary detection
_syllable_pattern = f"{_re_basic}(?=[{x0_1}{x0_2}{x0_3}{x0_4}{x0_5}{x1}]|\\s|[^\\u0E80-\\u0EFF]|$|{_re_lookahead})"

# Compile the regex
SYLLABLE_REGEX = re.compile(_syllable_pattern)

# Simple syllable regex for validation (without lookahead)
SIMPLE_SYLLABLE_REGEX = re.compile(_re_basic)


def normalize_tone_marks(text: str) -> str:
    """
    Normalize tone mark order in text.
    
    Some renderers place tone marks on top regardless of input order,
    leading to incorrect sequences like consonant-tonemark-vowel instead
    of the correct consonant-vowel-tonemark.
    
    :param str text: Text to normalize
    :return: Normalized text
    :rtype: str
    """
    pattern = f"([{CONSONANTS}])([{TONE_MARKS}])([{VOWELS_COMBINING}])"
    return re.sub(pattern, r"\1\3\2", text)


def syllable_tokenize(text: str, normalize: bool = False) -> List[str]:
    """
    Split Lao text into syllables.
    
    This implements a regular expression based algorithm to segment Lao text
    into syllables, based on the one described in PHISSAMAY et al:
    "Syllabification of Lao Script for Line Breaking".
    
    :param str text: Lao text to split into syllables
    :param bool normalize: Whether to normalize tone mark order (default: False)
    :return: List of Lao syllables
    :rtype: List[str]
    
    :Example:
    ::
    
        from laonlp.tokenize import syllable_tokenize
        
        text = "ສະບາຍດີ"
        print(syllable_tokenize(text))  # ['ສະ', 'ບາຍ', 'ດີ']
        
        text = "ພາສາລາວໃນປັດຈຸບັນ"
        print(syllable_tokenize(text))  # ['ພາ', 'ສາ', 'ລາວ', 'ໃນ', 'ປັດ', 'ຈຸ', 'ບັນ']
    """
    if not text:
        return []
    
    # Apply Unicode NFC normalization
    text = unicode_normalize("NFC", text)
    
    # Optionally normalize tone marks
    if normalize:
        text = normalize_tone_marks(text)
    
    # Remove zero-width spaces
    text = text.replace("\u200B", "")
    
    # Find all syllables
    syllables = SYLLABLE_REGEX.findall(text)
    
    return syllables
