# The code fellow https://www.laoconverter.info/moh2020.html
# TODO: Add Diphthong ເxັຽ, xຽx ເxຍ​ and more
from laonlp.util import remove_tone_mark
import re
from pythainlp.tokenize import Tokenizer

TONE_MARKS = "່້"+"໊໋"
CONSONANTS = "ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ"
VOWELS_COMBINING = "ັ"+"ິີ"+"ຶືຸ"+"ູົໍ"
VOWELS = "ະັາ"+"ຳິີ"+"ຶືຸ"+"ູົຼ"+"ຽເແ"+"ໂໃໄ"+"ໍ"
NUMBERS = "໑໒໓໔໕໖໗໘໙໐" # 1234567890
CANCELLATION_MARK = "\u0ECC"

consonants = { # Initial position 	[ipa, bgn, lc,moh2020], Final position [ipa, bgn, lc,moh2020]
    "ກ":[[["k"],["k"],["k"]],["k"],[["k"],["k"],["k"],["k"]]],
    "ຂ":[[["kʰ"],["kh"],["kh"],["kh"]],[["k"],["k"],["k"],["kh"]]],
    "ຄ":[[["kʰ"],["kh"],["kh"],["kh"]],[["k"],["k"],["k"]],["kh"]],
    "ງ":[[["ŋ"],["ng"],["ng"],["ng"]],[["ŋ"],["ng"],["ng"],["ng"]]],
    "ຈ":[[["tɕ"],["ch"],["ch"],["ch"]],[["t"],["t"],["c"],["ch"]]],
    "ສ":[[["s"],["s"],["s"],["s"]],[["t"],["t"],["s"],["s"]]],
    "ຊ":[[["s"],["x"],["s"],["x"]],[["t"],["t"],["s"],["x"]]],
    "ຍ":[[["ɲ"],["gn"],["ny"],["ny"]],[["j"],["y"],["i"],["y"]]],
    "ດ":[[["d"],["d"],["d"],["d"]],[["t"],["t"],["t"],["t"]]],
    "ຕ":[[["t"],["t"],["t"],["t"]],[["t"],["t"],["t"],["-"]]],
    "ຖ":[[["tʰ"],["th"],["th"],["th"]],[["t"],["t"],["th"],["th"]]],
    "ທ":[[["tʰ"],["th"],["t"],["th"]],[["t"],["t"],["th"],["th"]]],
    "ນ":[[["n"],["n"],["n"],["n"]],[["n"],["ne"],["n"],["n"]]],
    "ບ":[[["b"],["b"],["b"],["b"]],[["p"],["p"],["b"],["p"]]],
    "ປ":[[["p"],["p"],["p"],["p"]],[["p"],["p"],["p"],["p"]]],
    "ຜ":[[["pʰ"],["ph"],["ph"],["ph"]],[["-"],["-"],["ph"],["ph"]]],
    "ຝ":[[["f"],["f"],["f"],["f"]],[["p"],["p"],["f"],["f"]]],
    "ພ":[[["pʰ"],["ph"],["ph"],["ph"]],[["p"],["p"],["ph"],["ph"]]],
    "ຟ":[[["f"],["f"],["f"],["f"]],[["p"],["p"],["f"],["f"]]],
    "ມ":[[["m"],["m"],["m"],["m"]],[["m"],["m"],["m"],["m"]]],
    "ຢ":[[["j"],["y"],["y"],["y"]],[["-"],["-"],["y"],["y"]]],
    "ຣ":[[["r","l"],["r"],["r"],["r"]],[["n"],["ne"],["n","r"],["r"]]],
    "ລ":[[["l"],["l"],["l"],["l"]],[["n"],["ne"],["n","l"],["l"]]],
    "ວ":[[["ʋ","w"],["v"],["v","w"],["v"]],[["-"],["-"],["w"],["v","o"]]],
    "ຫ":[[["h"],["h"],["h"],["h"]],[["-"],["-"],["h"],["h"]]],
    "ອ":[[["ʔ"],["-"],["-"],["-"]],[["-"],["-"],["o","-"],["-"]]],
    "ຮ":[[["h"],["h"],["h"],["h"]],[["-"],["-"],["h"],["h"]]],
    "ຫງ":[[["ŋ"],["ng"],["ng"],["ng"]],[]],
    "ຫຍ":[[["ɲ"],["gn"],["ny"],["ny"]],[]],
    "ໜ":[[["n"],["n"],["n"],["n"]],[]],
    "ຫນ":[[["n"],["n"],["n"],["n"]],[]],
    "ໝ":[[["m"],["m"],["m"],["m"]],[]],
    "ຫມ":[[["m"],["m"],["m"],["m"]],[]],
    "ຫຼ":[[["l"],["l"],["l"],["l"]],[]],
    "ຫລ":[[["l"],["l"],["l"],["l"]],[]],
    "ຫວ":[[["ʋ","w"],["v"],["v","w"],["v"]],[]],
}

_consonants = Tokenizer(consonants.keys(), engine="mm")

vowel = {
    "ກະ":["a","a","a","a",1],
    "ກັກ":["a","a","a","a",2],
    "ກິ":["i","i","i","i",1],
    "ກຶ":["ɯ","u","ư","u",1],
    "ກຸ":["u","ou","u","ou",1],
    "ເກະ":["e","é","e","e",1],
    "ເກັກ":["e","é","e","e",1],
    "ແກະ":["ɛ","è","æ","e",1],
    "ແກັກ":["ɛ","è","æ","e",1],
    "ໂກະ":["o","ô","o","o",1],
    "ກົກ":["o","ô","o","o",2],
    "ເກາະ":["ɔ","o","o̜","o",1],
    "ກັອກ":["ɔ","o","o̜","o",2],
    "ເກິະ":["ɤ","eu","œ","eu",1],
    "ເກິກ":["ɤ","eu","œ","eu",1],
    "ເກົາ":["aw","ao","ao","ao",1],
    "ກໍາ":["am","am","am","am",1],
    "ກາ":["aː","a","ā","a",1],
    "ກີ":["iː","i","ī","i",1],
    "ກື":["ɯː","u","ư̄","u",1],
    "ກູ":["uː","ou","ū","ou",1],
    "ເກ":["eː","é","ē","e",1],
    "ແກ":["ɛː","è","ǣ","e",1],
    "ໂກ":["oː","ô","ō","o",1],
    "ກໍ":["ɔː","o","ō̜","o",1],
    "ກອກ":["ɔː","o","ō̜","o",2],
    "ເກີ":["ɤː","eu","œ̄","eu",1],
    "ເກືກ":["ɤː","eu","œ̄","eu",1],
    "ເກັຽະ":["iə","ia","ia","ia",1],
    "ກັຽກ":["iə","ia","ia","ia",2],
    "ເກຶອະ":["ɯə","ua","ưa","ua",1],
    "ເກຶອກ":["ɯə","ua","ưa","ua",1],
    "ກົວະ":["uə","oua","ua","oua",1],
    "ກັວກ":["uə","oua","ua","oua",2],
    "ໄກ":["aj","ai","ai","ai",1],
    "ໃກ":["aj","ai","ai","ai",1],
    "ກັຍ":["aj","ai","ai","ai",1],
    "ເກັຽ":["iːə","ia","īa","ia",1],
    "ກຽກ":["iːə","ia","īa","ia",2],
    "ເກຍ":["iːə","ia","īa","ia",1],
    "ເກືອ":["ɯːə","ua","ư̄a","ua",1],
    "ກົວ":["uːə","oua","ūa","oua",1],
    "ກວກ":["uːə","oua","ūa","oua",2],
    "ກາຍ":["aːj","ai","āi","ay",1],
    "ກາຽ":["-","ai","āi","ai",1],
    "ເກັຍ":["iə","ia","ia","ia",1],
}

def move_group(text,c):
    n = text.count("ກ")
    _t1 = ""
    if c == 1:
        for i in range(n):
            _t1 += "\\"+str(i+1)
        _t1 += "*"
    else:
        _t1 = "\\1"+"*"+"\\2"
    return _t1


_new_vowel_ipa = sorted([[i.replace("ກ","(["+CONSONANTS+"])"),move_group(i,j[-1]).replace("*",j[0])] for i,j in vowel.items()],key=lambda tup: len(tup[0]), reverse=True)
_new_vowel_bgn = sorted([[i.replace("ກ","(["+CONSONANTS+"])"),move_group(i,j[-1]).replace("*",j[2])] for i,j in vowel.items()],key=lambda tup: len(tup[0]), reverse=True)
_new_vowel_lc = sorted([[i.replace("ກ","(["+CONSONANTS+"])"),move_group(i,j[-1]).replace("*",j[2])] for i,j in vowel.items()],key=lambda tup: len(tup[0]), reverse=True)
_new_vowel_moh2020 = sorted([[i.replace("ກ","(["+CONSONANTS+"])"),move_group(i,j[-1]).replace("*",j[3])] for i,j in vowel.items()],key=lambda tup: len(tup[0]), reverse=True)

def _replace_vowels(word: str,mode:str="ipa") -> str:
    _d = None
    if mode == "ipa":
        _d = _new_vowel_ipa
    elif mode == "bgn":
        _d = _new_vowel_bgn
    elif mode == "lc":
        _d = _new_vowel_lc
    elif mode == "moh2020":
        _d = _new_vowel_moh2020
    for vowel in _d:
        if bool(re.search(vowel[0],word)):
            print(vowel[0], vowel[1],word)
            word = re.sub(vowel[0], vowel[1], word,re.U)
            print(word)
            break
    return word

VOWELS_all =list(VOWELS_COMBINING+VOWELS)

def rom(text,tag="ipa"):
    tag_n = 0
    if tag == "ipa":
        tag_n = 0
    elif tag == "bgn":
        tag_n = 1
    elif tag == "lc":
        tag_n = 2
    elif tag == "moh2020":
        tag_n = 3
    _t = remove_tone_mark(text)
    _t = _replace_vowels(_t,tag)
    _text = ""
    _i = 0
    for i in _consonants.word_tokenize(_t):
        if i not in consonants.keys():
            _text+=i
        else:
            _text+=consonants[i][_i][tag_n][0]
        _i=1
    return _text