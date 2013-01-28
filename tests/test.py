#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
import os

# make sure to import romkan from ../romkan directory relative to this
# file
sys.path.insert(0,
               (os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)))))
from romkan import *

class RomkanTestCase(unittest.TestCase):
    
    def test_to_katakana(self):
        self.assertEqual(to_katakana("kanji"),
                         u"カンジ")
        self.assertEqual(to_katakana("kanzi"),
                         u"カンジ")
        self.assertEqual(to_katakana("kannji"),
                         u"カンジ")
        self.assertEqual(to_katakana("chie"),
                         u"チエ")
        self.assertEqual(to_katakana("tie"),
                         u"チエ")
        self.assertEqual(to_katakana("kyouju"),
                         u"キョウジュ")
        self.assertEqual(to_katakana("syuukyou"),
                         u"シュウキョウ")
        self.assertEqual(to_katakana("shuukyou"),
                         u"シュウキョウ")
        self.assertEqual(to_katakana("saichuu"),
                         u"サイチュウ")
        self.assertEqual(to_katakana("saityuu"),
                         u"サイチュウ")
        self.assertEqual(to_katakana("cheri-"),
                         u"チェリー")
        self.assertEqual(to_katakana("tyeri-"),
                         u"チェリー")
        self.assertEqual(to_katakana("shinrai"),
                         u"シンライ")
        self.assertEqual(to_katakana("sinrai"),
                         u"シンライ")
        self.assertEqual(to_katakana("hannnou"),
                         u"ハンノウ")
        self.assertEqual(to_katakana("han'nou"),
                         u"ハンノウ")
        
        self.assertEqual(to_katakana("wo"),
                         u"ヲ")
        self.assertEqual(to_katakana("we"),
                         u"ウェ")
        self.assertEqual(to_katakana("du"),
                         u"ヅ")
        self.assertEqual(to_katakana("she"),
                         u"シェ")
        self.assertEqual(to_katakana("di"),
                         u"ヂ")
        self.assertEqual(to_katakana("fu"),
                         u"フ")
        self.assertEqual(to_katakana("ti"),
                         u"チ")
        self.assertEqual(to_katakana("wi"),
                         u"ウィ")
        
        self.assertEqual(to_katakana("je"),
                         u"ジェ")
        self.assertEqual(to_katakana("e-jento"),
                         u"エージェント")
        
    def test_to_hiragana(self):
        self.assertEqual(to_hiragana("kanji"),
                         u"かんじ")
        self.assertEqual(to_hiragana("kanzi"),
                         u"かんじ")
        self.assertEqual(to_hiragana("kannji"),
                         u"かんじ")
        self.assertEqual(to_hiragana("chie"),
                         u"ちえ")
        self.assertEqual(to_hiragana("tie"),
                         u"ちえ")
        self.assertEqual(to_hiragana("kyouju"),
                         u"きょうじゅ")
        self.assertEqual(to_hiragana("syuukyou"),
                         u"しゅうきょう")
        self.assertEqual(to_hiragana("shuukyou"),
                         u"しゅうきょう")
        self.assertEqual(to_hiragana("saichuu"),
                         u"さいちゅう")
        self.assertEqual(to_hiragana("saityuu"),
                         u"さいちゅう")
        self.assertEqual(to_hiragana("cheri-"),
                         u"ちぇりー")
        self.assertEqual(to_hiragana("tyeri-"),
                         u"ちぇりー")
        self.assertEqual(to_hiragana("shinrai"),
                         u"しんらい")
        self.assertEqual(to_hiragana("sinrai"),
                         u"しんらい")
        self.assertEqual(to_hiragana("hannnou"),
                         u"はんのう")
        self.assertEqual(to_hiragana("han'nou"),
                         u"はんのう")
        
    def test_to_kana(self):
        self.assertEqual(to_kana("kanji"),
                         u"カンジ")
        self.assertEqual(to_kana("kanzi"),
                         u"カンジ")
        self.assertEqual(to_kana("kannji"),
                         u"カンジ")
        self.assertEqual(to_kana("chie"),
                         u"チエ")
        self.assertEqual(to_kana("tie"),
                         u"チエ")
        self.assertEqual(to_kana("kyouju"),
                         u"キョウジュ")
        self.assertEqual(to_kana("syuukyou"),
                         u"シュウキョウ")
        self.assertEqual(to_kana("shuukyou"),
                         u"シュウキョウ")
        self.assertEqual(to_kana("saichuu"),
                         u"サイチュウ")
        self.assertEqual(to_kana("saityuu"),
                         u"サイチュウ")
        self.assertEqual(to_kana("cheri-"),
                         u"チェリー")
        self.assertEqual(to_kana("tyeri-"),
                         u"チェリー")
        self.assertEqual(to_kana("shinrai"),
                         u"シンライ")
        self.assertEqual(to_kana("sinrai"),
                         u"シンライ")
        self.assertEqual(to_kana("hannnou"),
                         u"ハンノウ")
        self.assertEqual(to_kana("han'nou"),
                         u"ハンノウ")
        
        self.assertEqual(to_kana("wo"),
                         u"ヲ")
        self.assertEqual(to_kana("we"),
                         u"ウェ")
        self.assertEqual(to_kana("du"),
                         u"ヅ")
        self.assertEqual(to_kana("she"),
                         u"シェ")
        self.assertEqual(to_kana("di"),
                         u"ヂ")
        self.assertEqual(to_kana("fu"),
                         u"フ")
        self.assertEqual(to_kana("ti"),
                         u"チ")
        self.assertEqual(to_kana("wi"),
                         u"ウィ")
        
        self.assertEqual(to_kana("je"),
                         u"ジェ")
        self.assertEqual(to_kana("e-jento"),
                         u"エージェント")
        
    def test_to_hepburn(self):
        self.assertEqual(to_hepburn("kannzi"),
                         "kanji")
        self.assertEqual(to_hepburn("tie"),
                         "chie")
        
        self.assertEqual(to_hepburn("KANNZI"),
                         "kanji")
        self.assertEqual(to_hepburn("TIE"),
                         "chie")
        
        self.assertEqual(to_hepburn(u"カンジ"),
                         "kanji")
        self.assertEqual(to_hepburn(u"チエ"),
                         "chie")
        
        self.assertEqual(to_hepburn(u"かんじ"),
                         "kanji")
        self.assertEqual(to_hepburn(u"ちえ"),
                         "chie")

        self.assertEqual(to_hepburn(u"しゃしん"),
                         "shashin")
        self.assertEqual(to_hepburn(u"しゅっしょう"),
                         "shusshou")

    def test_to_kunrei(self):
        self.assertEqual(to_kunrei("kanji"),
                         "kanzi")
        self.assertEqual(to_kunrei("chie"),
                         "tie")
        
        self.assertEqual(to_kunrei("KANJI"),
                         "kanzi")
        self.assertEqual(to_kunrei("CHIE"),
                         "tie")
        
        self.assertEqual(to_kunrei(u"カンジ"),
                         "kanzi")
        self.assertEqual(to_kunrei(u"チエ"),
                         "tie")
        
        self.assertEqual(to_kunrei(u"かんじ"),
                         "kanzi")
        self.assertEqual(to_kunrei(u"ちえ"),
                         "tie")

        self.assertEqual(to_kunrei(u"しゃしん"),
                         "syasin")
        self.assertEqual(to_kunrei(u"しゅっしょう"),
                         "syussyou")

    def test_to_roma(self):
        self.assertEqual(to_roma(u"カンジ"),
                         "kanji")
        self.assertEqual(to_roma(u"チャウ"),
                         "chau")
        self.assertEqual(to_roma(u"ハンノウ"),
                         "han'nou")
        
        self.assertEqual(to_roma(u"かんじ"),
                         "kanji")
        self.assertEqual(to_roma(u"ちゃう"),
                         "chau")
        self.assertEqual(to_roma(u"はんのう"),
                         "han'nou")
        
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
