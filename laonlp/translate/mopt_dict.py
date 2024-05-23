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
from laonlp.corpus import mopt_dict


def dictionary(word: str, src: str, target: str) -> list:
    if src == "lao" and target == "eng":
        _temp = mopt_dict.get_lao_eng()
        if word not in list(_temp.keys()):
            return []
        return _temp[word]
    elif src == "eng" and target == "lao":
        _temp = mopt_dict.get_eng_lao()
        if word not in list(_temp.keys()):
            return []
        return _temp[word]
    else:
        return [word]
