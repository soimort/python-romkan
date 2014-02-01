#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .version import __version__
import re
from romkan.data import ROMKAN, KANROM, KUNREI, HEPBURN
from romkan.data import hira_strict, kata
from romkan.utils import is_romaji, is_kana
try:
    from functools import cmp_to_key
except ImportError:
    # for python < 3.2; nicked from python 3.2
    def cmp_to_key(mycmp):
        """Convert a cmp= function into a key= function"""
        class K(object):
            __slots__ = ['obj']
            def __init__(self, obj):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
            __hash__ = None
        return K



#
# Ruby/Romkan - a Romaji <-> Kana conversion library for Ruby.
#
# Copyright (C) 2001 Satoru Takabayashi <satoru@namazu.org>
#     All rights reserved.
#     This is free software with ABSOLUTELY NO WARRANTY.
#
# You can redistribute it and/or modify it under the terms of 
# the Ruby's licence.
#


# Sort in long order so that a longer Romaji sequence precedes.

_len_cmp = lambda x: -len(x)
ROMPAT = re.compile("|".join(sorted(ROMKAN.keys(), key=_len_cmp)) )

_kanpat_cmp = lambda x, y: (len(y) > len(x)) - (len(y) < len(x)) or (len(KANROM[x]) > len(KANROM[x])) - (len(KANROM[x]) < len(KANROM[x]))
KANPAT = re.compile("|".join(sorted(KANROM.keys(), key=cmp_to_key(_kanpat_cmp))))


KUNPAT = re.compile("|".join(sorted(KUNREI, key=_len_cmp)) )
HEPPAT = re.compile("|".join(sorted(HEPBURN, key=_len_cmp)) )

TO_HEPBURN = {}
TO_KUNREI = {}

for kun, hep in zip(KUNREI, HEPBURN):
    TO_HEPBURN[kun] = hep
    TO_KUNREI[hep] = kun

TO_HEPBURN.update( {'ti': 'chi' })


def normalize_double_n(str):
    """
    Normalize double n.
    """
    
    # Replace double n with n'
    str = re.sub("nn", "n'", str)
    # Remove unnecessary apostrophes
    str = re.sub("n'(?=[^aeiuoyn]|$)", "n", str)
    
    return str

def to_katakana(str):
    """
    Convert a Romaji (ローマ字) to a Katakana (片仮名).
    """
    
    str = str.lower()
    str = normalize_double_n(str)
    
    tmp = ROMPAT.sub(lambda x: ROMKAN[x.group(0)], str)
    return tmp

def to_hiragana(str):
    """
    Convert a Romaji (ローマ字) to a Hiragana (平仮名).
    """
    return hira_strict(to_katakana(str))

def to_kana(str):
    """
    Convert a Romaji (ローマ字) to a Katakana (片仮名). (same as to_katakana)
    """
    return to_katakana(str)

def to_hepburn(text):
    """
    Convert a Kana (仮名) or a Kunrei-shiki Romaji (訓令式ローマ字) to a Hepburn Romaji (ヘボン式ローマ字).
    """
    assert is_romaji(text) or is_kana(text)
    romaji = text = normalize_double_n(text.lower())
    if is_kana(text):
        katakana = kata(romaji)  # coerce to *kata*-kana
        romaji = KANPAT.sub(lambda x: KANROM[x.group(0)], katakana)
    # If unmodified, maybe it's a Kunrei-shiki Romaji -- convert it to a Hepburn Romaji
    if romaji == text:
        romaji = KUNPAT.sub(lambda x: TO_HEPBURN[x.group(0)], romaji)
    # Remove unnecessary apostrophes
    return re.sub("n'(?=[^aeiuoyn]|$)", "n", romaji)

def to_kunrei(str):
    """
    Convert a Kana (仮名) or a Hepburn Romaji (ヘボン式ローマ字) to a Kunrei-shiki Romaji (訓令式ローマ字).
    """
    
    tmp = kata(str)
    tmp = KANPAT.sub(lambda x: KANROM[x.group(0)], tmp)
    
    # Remove unnecessary apostrophes
    tmp = re.sub("n'(?=[^aeiuoyn]|$)", "n", tmp)
    
    # If unmodified, it's a Hepburn Romaji Romaji -- convert it to a Kunrei-shiki Romaji
    # If modified, it's also a Hepburn Romaji Romaji -- convert it to a Kunrei-shiki Romaji
    tmp = tmp.lower()
    tmp = normalize_double_n(tmp)
    tmp = HEPPAT.sub(lambda x: TO_KUNREI[x.group(0)], tmp)
    
    return tmp

def to_roma(str):
    """
    Convert a Kana (仮名) to a Hepburn Romaji (ヘボン式ローマ字).
    """
    
    tmp = kata(str)
    tmp = KANPAT.sub(lambda x: KANROM[x.group(0)], tmp)
    
    # Remove unnecessary apostrophes
    tmp = re.sub("n'(?=[^aeiuoyn]|$)", "n", tmp)
    
    return tmp
