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

Multi cut -- Lao word segmentation with maximum matching.
Forked from PyThaiNLP's multi_cut.py

Note: This module depends on pythainlp.util.Trie which is a required 
dependency of LaoNLP (pythainlp>=3.0.0 in requirements.txt).
"""

import re
from collections import defaultdict
from typing import Iterator, List

# Import Trie from PyThaiNLP - this is a core dependency of LaoNLP
from pythainlp.util import Trie


class LatticeString(str):
    """String that keeps possible tokenizations"""

    def __new__(cls, value, multi=None, in_dict=True):
        return str.__new__(cls, value)

    def __init__(self, value, multi=None, in_dict=True):
        self.unique = True
        if multi:
            self.multi = list(multi)
            if len(self.multi) > 1:
                self.unique = False
        else:
            self.multi = [value]
        self.in_dict = in_dict  # if in dictionary


_RE_NONLAO = r"""(?x)
[-a-zA-Z]+|       # Latin characters
\d+([,\.]\d+)*|   # numbers
[ \t]+|           # spaces
\r?\n             # newlines
"""
_PAT_NONLAO = re.compile(_RE_NONLAO)

# Constants for safe mode text chunking to prevent infinite loops
# These values are based on PyThaiNLP PR #302 which fixes the hanging issue
# with long texts containing many ambiguous tokenization points
_TEXT_LIMIT = 120  # Base chunk size for splitting long text
_TEXT_SCAN_LEFT = 20  # Look-back window to find optimal split point
_TEXT_SCAN_RIGHT = 20  # Look-ahead window to find optimal split point


def _multicut(
    text: str, custom_dict: Trie
) -> Iterator[LatticeString]:
    """Return LatticeString"""
    if not custom_dict:
        raise ValueError("custom_dict is required")

    len_text = len(text)
    words_at = defaultdict(list)  # main data structure

    def serialize(p, p2):  # helper function
        for w in words_at[p]:
            p_ = p + len(w)
            if p_ == p2:
                yield w
            elif p_ < p2:
                for path in serialize(p_, p2):
                    yield w + "/" + path

    q = {0}
    last_p = 0  # last position for yield
    while min(q) < len_text:
        p = min(q)
        q -= {p}  # q.pop, but for set

        for w in custom_dict.prefixes(text[p:]):
            words_at[p].append(w)
            q.add(p + len(w))

        len_q = len(q)

        if len_q == 1:
            q0 = min(q)
            yield LatticeString(text[last_p:q0], serialize(last_p, q0))
            last_p = q0
        elif len_q == 0:  # len(q) == 0 means not found in dictionary
            m = _PAT_NONLAO.match(text[p:])
            if m:  # non-Lao token
                i = p + m.span()[1]
            else:  # non-Lao token, find minimum skip
                for i in range(p, len_text):
                    ww = custom_dict.prefixes(text[i:])
                    m = _PAT_NONLAO.match(text[i:])
                    if ww or m:
                        break
                else:
                    i = len_text
            w = text[p:i]
            words_at[p].append(w)
            yield LatticeString(w, in_dict=False)
            last_p = i
            q.add(i)


def mmcut(text: str, custom_dict: Trie) -> List[str]:
    """
    Maximum matching word segmentation.
    
    :param text: text to be tokenized
    :type text: str
    :param custom_dict: tokenization dictionary
    :type custom_dict: Trie
    :return: list of segmented tokens
    :rtype: List[str]
    """
    res = []
    for w in _multicut(text, custom_dict):
        mm = min(w.multi, key=lambda x: x.count("/"))
        res.extend(mm.split("/"))
    return res


def segment(
    text: str, custom_dict: Trie, safe_mode: bool = False
) -> List[str]:
    """
    Dictionary-based maximum matching word segmentation.

    :param text: text to be tokenized
    :type text: str
    :param custom_dict: tokenization dictionary
    :type custom_dict: Trie
    :param safe_mode: True to avoid long wait for long continuous text (edge case); Default is False
    :type safe_mode: bool
    :return: list of segmented tokens
    :rtype: List[str]
    """
    if not text or not isinstance(text, str):
        return []

    if not custom_dict:
        raise ValueError("custom_dict is required")

    if not safe_mode:
        return mmcut(text, custom_dict)

    text_len = len(text)

    if text_len < (_TEXT_LIMIT + _TEXT_SCAN_RIGHT):
        # if the text is shorter than the limit,
        # tokenizes the whole text at once
        return mmcut(text, custom_dict)
    else:
        # if the text is longer than the limit,
        # breaks them into smaller chunks then tokenizes each chunk
        text_parts = []

        while text_len >= (_TEXT_LIMIT + _TEXT_SCAN_RIGHT):
            sample_start = _TEXT_LIMIT - _TEXT_SCAN_LEFT
            sample_end = _TEXT_LIMIT + _TEXT_SCAN_RIGHT
            sample = text[sample_start:sample_end]

            # find possible break positions
            cut_pos = sample_end

            # try to break by space first
            space_idx = sample.rfind(" ")
            if space_idx >= 0:
                cut_pos = sample_start + space_idx + 1
            else:
                tokens = mmcut(sample, custom_dict)
                token_max_idx = 0
                token_max_len = 0
                for i, token in enumerate(tokens):
                    if len(token) > token_max_len:
                        token_max_len = len(token)
                        token_max_idx = i

                # choose the position that covers longest token
                cut_pos = sample_start
                for i in range(0, token_max_idx):
                    cut_pos = cut_pos + len(tokens[i])

            text_parts.append(text[:cut_pos])
            text = text[cut_pos:]
            text_len = len(text)

        # append remaining text
        if text_len:
            text_parts.append(text)

        # tokenizes each text parts
        tokens = []
        for text_part in text_parts:
            tokens.extend(mmcut(text_part, custom_dict))

        return tokens
