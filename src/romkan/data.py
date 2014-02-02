#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import re
from romkan.compat import DictReader, unichr, unicode


HERE = os.path.abspath(os.path.dirname(__file__))
MAPPING = os.path.join(HERE, 'mapping.csv')
_len_cmp = lambda x: -len(x)


common = [unichr(c) for c in (0x3099, 0x309A, 0x309B, 0x309C, 0x30A0, 0x30FC)]
# Note: code points that would correspond to Hiragana VA (0x3097) and VI (0x3098) are unused
hiragana = [unichr(i) for i in range(0x3041, 0x3097)] + ['ゔぁ', 'ゔぃ', 'ゝ', 'ゞ'] + common
katakana = [unichr(i) for i in range(0x30A1, 0x30F9)] + ['ヽ', 'ヾ'] + common


h2k_dct = dict(zip(hiragana, katakana))
k2h_dct = dict(zip(katakana, hiragana))
to_hira_dct = dict(zip(hiragana + katakana, hiragana * 2))
to_kata_dct = dict(zip(hiragana + katakana, katakana * 2))


def get_converter(dct, strict=True):
    def convert(text):
        if not strict: 
            pat = re.compile("|".join(sorted(dct, key=_len_cmp)))
            return pat.sub(lambda x: dct[x.group(0)], text)
        assert isinstance(text, unicode) and len(text) > 0
        try:
            return ''.join([dct[c] for c in text])
        except KeyError:
            msg = hex(ord(c)) if len(text) == 1 else text
            raise UnicodeError("Invalid code point supplied: %s" % msg)
    return convert

h2k, k2h, hira_strict, kata_strict = map(get_converter, (h2k_dct, k2h_dct, to_hira_dct, to_kata_dct))
kata = get_converter(to_kata_dct, strict=False)

KANROM = dict([(r['Katakana'], r['Kunrei']) for r in DictReader(open(MAPPING))])
ROMKAN = dict([(r['Kunrei'], r['Katakana']) for r in DictReader(open(MAPPING))])

# FIXME - this replicates previous behavior but is incorrect because it mixes Hepburn and Kunrei schemes
KANROM.update(dict([(r['Katakana'], r['Hepburn']) for r in DictReader(open(MAPPING))]))
ROMKAN.update(dict([(r['Hepburn'], r['Katakana']) for r in DictReader(open(MAPPING))]))

# special modification
# wo -> ヲ, but ヲ/ウォ -> wo
# du -> ヅ, but ヅ/ドゥ -> du
# we -> ウェ, ウェ -> we
ROMKAN.update( {"du": "ヅ", "di": "ヂ", "fu": "フ", "ti": "チ",
                "wi": "ウィ", "we": "ウェ", "wo": "ヲ" } )


KUNREI = [r['Kunrei'] for r in DictReader(open(MAPPING))]
HEPBURN = [r['Hepburn'] for r in DictReader(open(MAPPING))]


if __name__ == "__main__":
    for row in DictReader(open('mapping.csv')):
        h, k = row['Hiragana'], row['Katakana']
        assert k == h2k(h) and h == k2h(k)
        assert k == kata_strict(k) and h == hira_strict(h)
        assert h == hira_strict(kata_strict(h))
        assert k == kata_strict(hira_strict(k))
