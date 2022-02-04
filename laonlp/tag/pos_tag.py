# -*- coding: utf-8 -*-
from typing import List, Tuple
from laonlp.corpus import get_path_corpus
from pythainlp.tag import PerceptronTagger


def pos_tag(
    words: List[str],
    engine: str = "perceptron",
    corpus: str = "SeqLabeling"
) -> List[Tuple[str, str]]:
    """
    Lao Part-of-speech

    We use lao corpus from https://github.com/FoVNull/SeqLabeling

    :param List[str] words:  a list of tokenized lao words
    :param str engine: engine of pos_tag (perceptron engine)
    :param str corpus: SeqLabeling (corpus from https://github.com/FoVNull/SeqLabeling) or yunshan_cup_2020 (corpus from https://github.com/GKLMIP/Yunshan-Cup-2020)

    :return: a list of tuples (word, POS tag)
    :rtype: List[tuple[str, str]]

    :Example:
    ::
        from laonlp.tokenize import word_tokenize
        from laonlp.tag import pos_tag

        sent = word_tokenize("ພາສາລາວໃນປັດຈຸບັນ.")
        pos_tag(sent)
        # output: [('ພາສາລາວ', 'N'), ('ໃນ', 'PRE'), ('ປັດຈຸບັນ', 'ADJ'), ('.', 'PUNCT')]
    """
    if corpus == "yunshan_cup_2020":
        _FILENAME = "ptagger_Yunshan-Cup_corpus.json"
    else:
        _FILENAME = "ptagger_SeqLabeling_corpus.json"
    _PATH = get_path_corpus(_FILENAME)
    _TAGGER = PerceptronTagger(path=_PATH)
    return _TAGGER.tag(words)
