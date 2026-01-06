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
from pythainlp.util import Trie
from laonlp.corpus import lao_words
from laonlp.tokenize.multi_cut import segment

_word_dict_trie = Trie(lao_words())
_RE_sent = re.compile(r"(?<=\.)(?!(?:\.|$))")


def word_tokenize(sent: str, safe_mode: bool = True) -> List[str]:
    """
    Lao word tokenize

    :param str sent: lao text
    :param bool safe_mode: True to avoid long wait for long continuous text (edge case); Default is True
    :return: returns a list of lao words
    :rtype: list

    :Example:
    ::

        from laonlp.tokenize import word_tokenize

        txt= "ພາສາລາວໃນປັດຈຸບັນ."
        print(word_tokenize(txt)) # ['ພາສາລາວ', 'ໃນ', 'ປັດຈຸບັນ', '.']
    """
    return segment(sent, custom_dict=_word_dict_trie, safe_mode=safe_mode)


def sent_tokenize(txt: str) -> List[str]:
    """
    Sentence tokenizer.

    Lao Text to sentence

    :param str sent: lao text
    :return: returns a list of lao sentence
    :rtype: list
    """
    sentences = []
    for part in _RE_sent.split(txt):
        sentences.append(part.strip())
    return sentences
