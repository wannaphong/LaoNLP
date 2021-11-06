# -*- coding: utf-8 -*-
from laonlp.tokenize import *
from laonlp.corpus import *
from laonlp.transliterate import *
from laonlp.tag import pos_tag

TONE_MARKS = "່້"+"໊໋"
CONSONANTS = "ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ"
VOWELS_COMBINING = "ັ"+"ິີ"+"ຶືຸ"+"ູົໍ"
VOWELS = "ະັາ"+"ຳິີ"+"ຶືຸ"+"ູົຼ"+"ຽເແ"+"ໂໃໄ"+"ໍ"