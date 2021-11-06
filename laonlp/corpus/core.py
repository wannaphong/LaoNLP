# -*- coding: utf-8 -*-
import os
from laonlp.corpus import laonlp_path


def get_path_corpus(file):
    return os.path.join(laonlp_path, "corpus", file)