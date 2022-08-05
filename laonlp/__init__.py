# -*- coding: utf-8 -*-
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