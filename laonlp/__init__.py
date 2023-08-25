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
from laonlp.tokenize import *
from laonlp.corpus import *
from laonlp.transliterate import *
from laonlp.tag import pos_tag
from laonlp.util import *

TONE_MARKS = "່້"+"໊໋"
CONSONANTS = "ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ"
VOWELS_COMBINING = "ັ"+"ິີ"+"ຶືຸ"+"ູົໍ"
VOWELS = "ະັາ"+"ຳິີ"+"ຶືຸ"+"ູົຼ"+"ຽເແ"+"ໂໃໄ"+"ໍ"
NUMBERS = "໑໒໓໔໕໖໗໘໙໐" # 1234567890
CANCELLATION_MARK = "\u0ECC"
# This is Obsolete consonants.
# You can read at https://en.wikipedia.org/wiki/Lao_script
lao_obsolete_consonants_mapping_thai = {
    "ຆ":"ฆ", # PALI GHA
    "ຉ":"ฉ", # PALI CHA
    "ຌ":"ฌ", # PALI JHA
    "ຎ":"ญ", # PALI NYA
    "ຏ":"ฏ", # PALI TTA
    "ຐ":"ฐ", # PALI TTHA
    "ຑ":"ฑ", # PALI DDA
    "ຒ":"ฒ", # PALI DDHA
    "ຓ":"ณ", # PALI NNA
    "ຘ":"ธ", # PALI DHA
    "ຠ":"ภ", # PALI BHA
    "ຨ":"ศ", # SANSKRIT SHA
    "ຩ":"ษ", # SANSKRIT SSA
    "ຬ":"ฬ", # PALI LLA
}