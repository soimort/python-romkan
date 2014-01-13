#!/usr/bin/env python

import os
import unittest
from ddt import ddt, data
from unicodecsv import DictReader
from romkan import to_kunrei, to_hepburn, to_hiragana, to_katakana
from romkan import is_vowel, is_consonant, expand_consonant


SEP = '/'   # Separates variants in the same CSV field
HERE = os.path.abspath(os.path.dirname(__file__))
TESTS_CSV = os.path.join(HERE, 'tests.csv')


def get_cases_from_csv(input_field, output_field):
    fh = open(TESTS_CSV, 'r')
    ucsv = DictReader(fh, delimiter=str('\t'))
    for row in ucsv:
        inputs, outputs = row[input_field], row[output_field]
        for i in inputs.split(SEP):
            if outputs != '':
                yield i, outputs.split(SEP)


@ddt
class ConversionTestCase(unittest.TestCase):

    @data(*list(get_cases_from_csv('hiragana', 'hepburn revised')))
    def test_hiragana_to_hepburn(self, row):
        in_text, expected = row
        self.assertIn(to_hepburn(in_text), expected)

    @data(*list(get_cases_from_csv('hiragana', 'kunrei-shiki')))
    def test_hiragana_to_kunrei(self, row):
        in_text, expected = row
        self.assertIn(to_kunrei(in_text), expected)

    @data(*list(get_cases_from_csv('hiragana', 'katakana')))
    def test_hiragana_to_katakana(self, row):
        in_text, expected = row
        self.assertIn(to_katakana(in_text), expected)

    @data(*list(get_cases_from_csv('katakana', 'hiragana')))
    def test_katakana_to_hiragana(self, row):
        in_text, expected = row
        self.assertIn(to_katakana(in_text), expected)

    @data(*list(get_cases_from_csv('wapuro', 'hiragana')))
    def test_wapuro_to_hiragana(self, row):
        in_text, expected = row
        self.assertIn(to_hiragana(in_text), expected)

    @data(*list(get_cases_from_csv('wapuro', 'katakana')))
    def test_wapuro_to_katakana(self, row):
        in_text, expected = row
        self.assertIn(to_katakana(in_text), expected)


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
