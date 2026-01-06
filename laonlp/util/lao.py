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
import unicodedata
from typing import List

TONE_MARKS = "່້"+"໊໋"
_tone_mark = str.maketrans({i: None for i in TONE_MARKS})


def remove_tone_mark(text: str) -> str:
    """
    Remove tone mark from Lao text

    :param str text: lao text
    :return: returns a lao text without tone mark.
    :rtype: str
    """
    return text.translate(_tone_mark)


def split_graphemes(text: str) -> List[str]:
    """
    Split Lao text into grapheme clusters.
    
    A grapheme cluster consists of a base character followed by any
    combining marks (such as tone marks and combining vowels).
    This ensures that characters with tone marks are not split apart.

    :param str text: lao text
    :return: returns a list of grapheme clusters
    :rtype: List[str]
    
    :Example:
    ::

        from laonlp.util import split_graphemes

        text = "ຜູ້"  # person with tone mark
        print(split_graphemes(text))  # ['ຜູ້']
        
        text = "ກ່ອນ"  # before with tone mark
        print(split_graphemes(text))  # ['ກ່', 'ອ', 'ນ']
    """
    if not text:
        return []
    
    graphemes = []
    current_grapheme = ""
    
    for char in text:
        category = unicodedata.category(char)
        # Mn = Mark, nonspacing (combining marks like tone marks and vowels)
        # Mc = Mark, spacing combining
        if category in ('Mn', 'Mc') and current_grapheme:
            # This is a combining mark, add to current grapheme
            current_grapheme += char
        else:
            # This is a base character, start new grapheme
            if current_grapheme:
                graphemes.append(current_grapheme)
            current_grapheme = char
    
    # Don't forget the last grapheme
    if current_grapheme:
        graphemes.append(current_grapheme)
    
    return graphemes
