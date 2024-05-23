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
import re
from typing import List
from pythainlp.tokenize import Tokenizer
from laonlp.corpus import lao_words

_word = Tokenizer(lao_words(), engine="mm")


def word_tokenize(sent: str) -> List[str]:
    """
    Lao word tokenize

    :param str sent: lao text
    :return: returns a list of lao words
    :rtype: list
    """
    return _word.word_tokenize(sent)


def sent_tokenize(txt: str) -> List[str]:
    """
    Sentence tokenizer.

    Lao Text to sentence

    :param str sent: lao text
    :return: returns a list of lao sentence
    :rtype: list
    """
    sentences = []
    for part in re.split(r"(?<=\.)(?!(?:\.|$))", txt):
        sentences.append(part.strip())
    return sentences
