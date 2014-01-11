#!/usr/bin/env python

import os
import unittest
from ddt import ddt, data
from unicodecsv import UnicodeReader
from romkan import to_roma, to_kunrei, to_hepburn, to_kana, to_hiragana, to_katakana
from romkan import is_vowel, is_consonant, expand_consonant


def open_csv(path):
    fh = open(path, 'r')
    ucsv = UnicodeReader(fh, delimiter=str('	'))
    return ucsv


HERE = os.path.abspath(os.path.dirname(__file__))
TO_ROMA = os.path.join(HERE, 'to_roma.csv')
TO_KUNREI = os.path.join(HERE, 'to_kunrei.csv')
TO_HEPBURN = os.path.join(HERE, 'to_hepburn.csv')
TO_KANA = os.path.join(HERE, 'to_kana.csv')
TO_HIRAGANA = os.path.join(HERE, 'to_hiragana.csv')
TO_KATAKANA = os.path.join(HERE, 'to_katakana.csv')


@ddt
class ConversionTestCase(unittest.TestCase):

    @data(*open_csv(TO_ROMA))
    def test_to_roma(self, row):
        in_text, expected = row
        self.assertEquals(to_roma(in_text), expected)

    @data(*open_csv(TO_KUNREI))
    def test_to_kunrei(self, row):
        in_text, expected = row
        self.assertEquals(to_kunrei(in_text), expected)

    @data(*open_csv(TO_HEPBURN))
    def test_to_hepburn(self, row):
        in_text, expected = row
        self.assertEquals(to_hepburn(in_text), expected)

    @data(*open_csv(TO_KANA))
    def test_to_kana(self, row):
        in_text, expected = row
        self.assertEquals(to_kana(in_text), expected)

    @data(*open_csv(TO_HIRAGANA))
    def test_to_hiragana(self, row):
        in_text, expected = row
        self.assertEquals(to_hiragana(in_text), expected)

    @data(*open_csv(TO_KATAKANA))
    def test_to_katakana(self, row):
        in_text, expected = row
        self.assertEquals(to_katakana(in_text), expected)


class RomkanTestCase(unittest.TestCase):
        
    def test_is_consonant(self):
        assert not is_consonant("a")
        assert is_consonant("k")
        
    def test_is_vowel(self):
        assert is_vowel("a")
        assert not is_vowel("z")
        
    def test_expand_consonant(self):
        self.assertEqual(sorted(expand_consonant("k")),
                         ['ka', 'ke', 'ki', 'ko', 'ku'])
        self.assertEqual(sorted(expand_consonant("s")),
                         ['sa', 'se', 'si', 'so', 'su'])
        self.assertEqual(sorted(expand_consonant("t")),
                         ['ta', 'te', 'ti', 'to', 'tu'])
        
        self.assertEqual(sorted(expand_consonant("ky")),
                         ['kya', 'kyo', 'kyu'])
        self.assertEqual(sorted(expand_consonant("kk")),
                         ["kka", "kke", "kki", "kko", "kku"])
        self.assertEqual(sorted(expand_consonant("sh")),
                         ["sha", "she", "shi", "sho", "shu"])
        self.assertEqual(sorted(expand_consonant("sy")),
                         ["sya", "sye", "syo", "syu"])
        self.assertEqual(sorted(expand_consonant("ch")),
                         ["cha", "che", "chi", "cho", "chu"])

if __name__ == '__main__':
    unittest.main()
