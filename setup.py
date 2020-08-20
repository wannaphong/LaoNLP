# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()

requirements = [
    "pythainlp>=2.1.0"
]
setup(
    name="LaoNLP",
    version="0.1-dev1",
    description="Lao Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/wannaphong/laonlp",
    packages=find_packages(),
    test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "laonlp.corpus": [
            "Lao-Dictionary.txt",
            "lo_spellcheck_dict.txt"
        ]
    },
    install_requires=requirements,
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
        "Development Status :: 3 - Alpha",
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
