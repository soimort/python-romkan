python-romkan
=============

`python-romkan <https://github.com/soimort/python-romkan>`_ is a Romaji/Kana conversion library for Python, which is used to convert a Japanese Romaji (ローマ字) string to a Japanese Kana (仮名) string or vice versa.

It is the Pythonic port of `Ruby/Romkan <http://0xcc.net/ruby-romkan/index.html.en>`_, originally authored by Satoru Takabayashi and `ported <http://lilyx.net/python-romkan/>`_ by Masato Hagiwara.

`python-romkan <https://github.com/soimort/python-romkan>`_ works on Python 2 and Python 3 (fully tested on **Python 2.6**, **2.7**, **3.2**, **3.3** and **PyPy**). It handles both Katakana (片仮名) and Hiragana (平仮名) with the Hepburn (ヘボン式) romanization system, as well as the modern Kunrei-shiki (訓令式) romanization system.

Project homepage: http://www.soimort.org/python-romkan

Fork me on GitHub: https://github.com/soimort/python-romkan

.. image:: https://api.travis-ci.org/soimort/python-romkan.png



Installation
------------

#) Install via `Pip <http://www.pip-installer.org/>`_::

    $ pip install romkan
    
#) Install via `EasyInstall <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install romkan
    
#) Install from Git::

    $ git clone git://github.com/soimort/python-romkan.git
    $ python setup.py install



Usage
-----

Python 3.x::

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

Python 2.x::

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



API Reference
-------------

* **to_katakana(string)**

Convert a Romaji (ローマ字) to a Katakana (片仮名).

* **to_hiragana(string)**

Convert a Romaji (ローマ字) to a Hiragana (平仮名).

* **to_kana(string)**

Convert a Romaji (ローマ字) to a Katakana (片仮名). (same as *to_katakana*)

* **to_hepburn(string)**

Convert a Kana (仮名) or a Kunrei-shiki Romaji (訓令式ローマ字) to a Hepburn Romaji (ヘボン式ローマ字).

* **to_kunrei(string)**

Convert a Kana (仮名) or a Hepburn Romaji (ヘボン式ローマ字) to a Kunrei-shiki Romaji (訓令式ローマ字).

* **to_roma(string)**

Convert a Kana (仮名) to a Hepburn Romaji (ヘボン式ローマ字).



License
-------

`python-romkan <https://github.com/soimort/python-romkan>`_ is licensed under the `BSD license <https://raw.github.com/soimort/python-romkan/master/LICENSE>`_.
