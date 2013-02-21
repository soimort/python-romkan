#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
                         "カンジ")
        self.assertEqual(to_katakana("kanzi"),
                         "カンジ")
        self.assertEqual(to_katakana("kannji"),
                         "カンジ")
        self.assertEqual(to_katakana("chie"),
                         "チエ")
        self.assertEqual(to_katakana("tie"),
                         "チエ")
        self.assertEqual(to_katakana("kyouju"),
                         "キョウジュ")
        self.assertEqual(to_katakana("syuukyou"),
                         "シュウキョウ")
        self.assertEqual(to_katakana("shuukyou"),
                         "シュウキョウ")
        self.assertEqual(to_katakana("saichuu"),
                         "サイチュウ")
        self.assertEqual(to_katakana("saityuu"),
                         "サイチュウ")
        self.assertEqual(to_katakana("cheri-"),
                         "チェリー")
        self.assertEqual(to_katakana("tyeri-"),
                         "チェリー")
        self.assertEqual(to_katakana("shinrai"),
                         "シンライ")
        self.assertEqual(to_katakana("sinrai"),
                         "シンライ")
        self.assertEqual(to_katakana("hannnou"),
                         "ハンノウ")
        self.assertEqual(to_katakana("han'nou"),
                         "ハンノウ")
        
        self.assertEqual(to_katakana("wo"),
                         "ヲ")
        self.assertEqual(to_katakana("we"),
                         "ウェ")
        self.assertEqual(to_katakana("du"),
                         "ヅ")
        self.assertEqual(to_katakana("she"),
                         "シェ")
        self.assertEqual(to_katakana("di"),
                         "ヂ")
        self.assertEqual(to_katakana("fu"),
                         "フ")
        self.assertEqual(to_katakana("ti"),
                         "チ")
        self.assertEqual(to_katakana("wi"),
                         "ウィ")
        
        self.assertEqual(to_katakana("je"),
                         "ジェ")
        self.assertEqual(to_katakana("e-jento"),
                         "エージェント")
        
    def test_to_hiragana(self):
        self.assertEqual(to_hiragana("kanji"),
                         "かんじ")
        self.assertEqual(to_hiragana("kanzi"),
                         "かんじ")
        self.assertEqual(to_hiragana("kannji"),
                         "かんじ")
        self.assertEqual(to_hiragana("chie"),
                         "ちえ")
        self.assertEqual(to_hiragana("tie"),
                         "ちえ")
        self.assertEqual(to_hiragana("kyouju"),
                         "きょうじゅ")
        self.assertEqual(to_hiragana("syuukyou"),
                         "しゅうきょう")
        self.assertEqual(to_hiragana("shuukyou"),
                         "しゅうきょう")
        self.assertEqual(to_hiragana("saichuu"),
                         "さいちゅう")
        self.assertEqual(to_hiragana("saityuu"),
                         "さいちゅう")
        self.assertEqual(to_hiragana("cheri-"),
                         "ちぇりー")
        self.assertEqual(to_hiragana("tyeri-"),
                         "ちぇりー")
        self.assertEqual(to_hiragana("shinrai"),
                         "しんらい")
        self.assertEqual(to_hiragana("sinrai"),
                         "しんらい")
        self.assertEqual(to_hiragana("hannnou"),
                         "はんのう")
        self.assertEqual(to_hiragana("han'nou"),
                         "はんのう")
        
    def test_to_kana(self):
        self.assertEqual(to_kana("kanji"),
                         "カンジ")
        self.assertEqual(to_kana("kanzi"),
                         "カンジ")
        self.assertEqual(to_kana("kannji"),
                         "カンジ")
        self.assertEqual(to_kana("chie"),
                         "チエ")
        self.assertEqual(to_kana("tie"),
                         "チエ")
        self.assertEqual(to_kana("kyouju"),
                         "キョウジュ")
        self.assertEqual(to_kana("syuukyou"),
                         "シュウキョウ")
        self.assertEqual(to_kana("shuukyou"),
                         "シュウキョウ")
        self.assertEqual(to_kana("saichuu"),
                         "サイチュウ")
        self.assertEqual(to_kana("saityuu"),
                         "サイチュウ")
        self.assertEqual(to_kana("cheri-"),
                         "チェリー")
        self.assertEqual(to_kana("tyeri-"),
                         "チェリー")
        self.assertEqual(to_kana("shinrai"),
                         "シンライ")
        self.assertEqual(to_kana("sinrai"),
                         "シンライ")
        self.assertEqual(to_kana("hannnou"),
                         "ハンノウ")
        self.assertEqual(to_kana("han'nou"),
                         "ハンノウ")
        
        self.assertEqual(to_kana("wo"),
                         "ヲ")
        self.assertEqual(to_kana("we"),
                         "ウェ")
        self.assertEqual(to_kana("du"),
                         "ヅ")
        self.assertEqual(to_kana("she"),
                         "シェ")
        self.assertEqual(to_kana("di"),
                         "ヂ")
        self.assertEqual(to_kana("fu"),
                         "フ")
        self.assertEqual(to_kana("ti"),
                         "チ")
        self.assertEqual(to_kana("wi"),
                         "ウィ")
        
        self.assertEqual(to_kana("je"),
                         "ジェ")
        self.assertEqual(to_kana("e-jento"),
                         "エージェント")
        
    def test_to_hepburn(self):
        self.assertEqual(to_hepburn("kannzi"),
                         "kanji")
        self.assertEqual(to_hepburn("tie"),
                         "chie")
        
        self.assertEqual(to_hepburn("KANNZI"),
                         "kanji")
        self.assertEqual(to_hepburn("TIE"),
                         "chie")
        
        self.assertEqual(to_hepburn("カンジ"),
                         "kanji")
        self.assertEqual(to_hepburn("チエ"),
                         "chie")
        
        self.assertEqual(to_hepburn("かんじ"),
                         "kanji")
        self.assertEqual(to_hepburn("ちえ"),
                         "chie")

        self.assertEqual(to_hepburn("しゃしん"),
                         "shashin")
        self.assertEqual(to_hepburn("しゅっしょう"),
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
        
        self.assertEqual(to_kunrei("カンジ"),
                         "kanzi")
        self.assertEqual(to_kunrei("チエ"),
                         "tie")
        
        self.assertEqual(to_kunrei("かんじ"),
                         "kanzi")
        self.assertEqual(to_kunrei("ちえ"),
                         "tie")
        
        self.assertEqual(to_kunrei("しゃしん"),
                         "syasin")
        self.assertEqual(to_kunrei("しゅっしょう"),
                         "syussyou")
        
    def test_to_roma(self):
        self.assertEqual(to_roma("カンジ"),
                         "kanji")
        self.assertEqual(to_roma("チャウ"),
                         "chau")
        self.assertEqual(to_roma("ハンノウ"),
                         "han'nou")
        
        self.assertEqual(to_roma("かんじ"),
                         "kanji")
        self.assertEqual(to_roma("ちゃう"),
                         "chau")
        self.assertEqual(to_roma("はんのう"),
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
