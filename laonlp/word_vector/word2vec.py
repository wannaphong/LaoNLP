# -*- coding: utf-8 -*-
from typing import List
import gensim
from huggingface_hub import hf_hub_download


class Word2Vec:
    """
    Word2Vec
    """
    def __init__(self, model: str, corpus: str="oscar"):
        """
        :param str model: model name (cbow or skip-gram)
        :param str corpus: corpus name (oscar)
        """
        self.model = model
        self.corpus = corpus
        if self.corpus not in ["oscar"]:
            raise NotImplementedError("LaoNLP doesn't support %s corpus." % self.corpus)
        self.load_model(self.model)
    
    def load_model(self, model: str):
        """
        Load Word2Vec model

        :param str model: model name (cbow or skip-gram)
        """
        if model=="cbow":
            self.model_path = hf_hub_download(repo_id="wannaphong/Lao-Word-Embedding", filename="lao_oscar_cbow_model.bin")
        elif model=="skip-gram":
            self.model_path = hf_hub_download(repo_id="wannaphong/Lao-Word-Embedding", filename="lao_oscar_skipgram_model.bin")
        else:
            raise NotImplementedError("LaoNLP doesn't support %s model." % model)
        self.model_wav2vec = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(self.model_path, binary=True, encoding='utf-8-sig', unicode_errors='ignore')
    
    def get_model(self):
        """
        Get gensim.models.keyedvectors.KeyedVectors class
        """
        return self.model_wav2vec
    
    def doesnt_match(self, words: List[str]) -> str:
        """
        Get donesn't match

        :param list words: list words

        :return: return word that donesn't match.
        :rtype: str
        """
        return self.model_wav2vec.doesnt_match(words)
    
    def most_similar_cosmul(self, positive: List[str], negative: List[str]):
        return self.model_wav2vec.most_similar_cosmul(
            positive=positive, negative=negative
        )
    
    def similarity(self, word1: str, word2: str) -> float:
        """
        Find similarity between word pairs.

        :param str word1: first word
        :param str word2: second word

        :return: return similarity
        :rtype: float
        """
        return self.model_wav2vec.similarity(word1, word2)