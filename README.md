# python-romkan

[![Build Status](https://api.travis-ci.org/soimort/python-romkan.png)](https://travis-ci.org/soimort/python-romkan) [![PyPI version](https://badge.fury.io/py/romkan.png)](http://badge.fury.io/py/romkan)

[python-romkan](https://github.com/soimort/python-romkan) is a Romaji/Kana conversion library for Python, which is used to convert a Japanese Romaji (ローマ字) string to a Japanese Kana (仮名) string or vice versa.

It is the Pythonic port of [Ruby/Romkan](http://0xcc.net/ruby-romkan/index.html.en), originally authored by Satoru Takabayashi and [ported](http://lilyx.net/python-romkan/) by Masato Hagiwara.

[python-romkan](https://github.com/soimort/python-romkan) works on Python 2 and Python 3 (fully tested on __Python 2.6__, __2.7__, __3.2__, __3.3__ and __PyPy__). It handles both Katakana (片仮名) and Hiragana (平仮名) with the Hepburn (ヘボン式) romanization system, as well as the modern Kunrei-shiki (訓令式) romanization system.

Project homepage: <http://www.soimort.org/python-romkan>

Fork me on GitHub: <https://github.com/soimort/python-romkan>



## Installation

### 1. Install via [Pip](http://www.pip-installer.org/):

    $ pip install romkan
    
### 2. Install via [EasyInstall](http://pypi.python.org/pypi/setuptools):

    $ easy_install romkan
    
### 3. Install from Git:

    $ git clone git://github.com/soimort/python-romkan.git
    $ python setup.py install


## Usage

Python 3.x:

    $ python
    >>> import romkan
    >>> print(romkan.to_roma("にんじゃ"))
    ninja
    >>> print(romkan.to_hepburn("にんじゃ"))
    ninja
    >>> print(romkan.to_kunrei("にんじゃ"))
    ninzya
    >>> print(romkan.to_hiragana("ninja"))
    にんじゃ
    >>> print(romkan.to_katakana("ninja"))
    ニンジャ

Python 2.x:

    $ python2
    >>> import romkan
    >>> print romkan.to_roma(u"にんじゃ")
    ninja
    >>> print romkan.to_hepburn(u"にんじゃ")
    ninja
    >>> print romkan.to_kunrei(u"にんじゃ")
    ninzya
    >>> print romkan.to_hiragana("ninja")
    にんじゃ
    >>> print romkan.to_katakana("ninja")
    ニンジャ



## API Reference

* __to_katakana(string)__

Convert a Romaji (ローマ字) to a Katakana (片仮名).

* __to_hiragana(string)__

Convert a Romaji (ローマ字) to a Hiragana (平仮名).

* __to_kana(string)__

Convert a Romaji (ローマ字) to a Katakana (片仮名). (same as _to\_katakana_)

* __to_hepburn(string)__

Convert a Kana (仮名) or a Kunrei-shiki Romaji (訓令式ローマ字) to a Hepburn Romaji (ヘボン式ローマ字).

* __to_kunrei(string)__

Convert a Kana (仮名) or a Hepburn Romaji (ヘボン式ローマ字) to a Kunrei-shiki Romaji (訓令式ローマ字).

* __to_roma(string)__

Convert a Kana (仮名) to a Hepburn Romaji (ヘボン式ローマ字).



## License

[python-romkan](https://github.com/soimort/python-romkan) is licensed under the [BSD license](https://raw.github.com/soimort/python-romkan/master/LICENSE).
