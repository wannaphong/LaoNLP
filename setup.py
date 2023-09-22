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
from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()

with open("requirements.txt","r",encoding="utf-8-sig") as f:
    requirements = [i.strip() for i in f.readlines()]

extras = {
    "anyascii": ["anyascii>=0.3.2"],
    "word_vector": ["gensim", "huggingface-hub"],
    "full": [
        "anyascii>=0.3.2",
        "gensim",
        "huggingface-hub"
    ]
}

setup(
    name="LaoNLP",
    version="1.1.1",
    description="Lao Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong",
    author_email="wannaphong@yahoo.com",
    url="https://github.com/wannaphong/laonlp",
    packages=find_packages(),
    test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "laonlp": [
            "corpus/*",
        ]
    },
    install_requires=requirements,
    extras_require=extras,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "lao",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "Lao language",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Documentation": "https://github.com/wannaphong/LaoNLP/wiki",
        "Source": "https://github.com/wannaphong/LaoNLP",
        "Bug Reports": "https://github.com/wannaphong/LaoNLP/issues",
    },
)
