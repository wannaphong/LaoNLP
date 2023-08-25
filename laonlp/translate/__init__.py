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
__all__ = [
    "word_dictionary",
]
from laonlp.translate.mopt_dict import dictionary

def word_dictionary(word: str, src: str, target: str, name: str = "mopt_laos")->list:
    """
    Word dictionary

    :param str word: text
    :param str src: src language (lao is Lao, eng is English)
    :param str name: Word dictionary (the default dict is mopt_laos.)
    :return: return word
    :rtype: str
    """
    return dictionary(word, src, target)