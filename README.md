# LaoNLP
[![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&link=https://github.com/sponsors/wannaphong/)](https://github.com/sponsors/wannaphong/)
[![Downloads](https://pepy.tech/badge/laonlp)](https://pepy.tech/project/laonlp)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6833407.svg)](https://doi.org/10.5281/zenodo.6833407)
[![Coverage Status](https://coveralls.io/repos/github/wannaphong/LaoNLP/badge.svg?branch=master)](https://coveralls.io/github/wannaphong/LaoNLP?branch=master)

Lao language Natural Language Processing (NLP)

## Features

- Word tokenizer
- Sentence tokenizer
- Part-of-speech
- Lao to Thai script
- Thai to Lao script
- Word dictionary
- Word Vector

## Install
```
pip install laonlp
```

### Installation Options

Some functionalities, like word vectors, may require extra packages. To install those requirements, specify a set of `[name]` immediately after `laonlp`:

```
pip install laonlp[extra1,extra2,...]
```

<details>
  <summary>List of possible <code>extras</code></summary>

- `full` (install everything)
- `anyascii` (for support of the `anyascii` engine of Lao transliteration functionalities)
- `word_vector` (for support of word vector functionalities)
</details>

For dependency details, look at `extras` variable in [`setup.py`](https://github.com/wannaphong/LaoNLP/blob/master/setup.py).

Documentation: https://github.com/wannaphong/LaoNLP/wiki

## Citations

If you use `LaoNLP` in your project or publication, please cite the library as follows

```
Wannaphong Phatthiyaphaibun. (2022). LaoNLP: Lao language Natural Language Processing. Zenodo. https://doi.org/10.5281/zenodo.6833407
```

or BibTeX entry:

``` bib
@misc{wannaphong_phatthiyaphaibun_2022_6833407,
  author       = {Wannaphong Phatthiyaphaibun},
  title        = {LaoNLP: Lao language Natural Language Processing},
  month        = jul,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.6833407},
  url          = {https://doi.org/10.5281/zenodo.6833407}
}
```

## License

```
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
 ```
