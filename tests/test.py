#!/usr/bin/env python

import unittest

from romkan import *

class RomkanTestCase(unittest.TestCase):
    
    def test_to_katakana(self):
        assert to_katakana("kanji") == u"カンジ"
        assert to_katakana("kanzi") == u"カンジ"
        assert to_katakana("kannji") == u"カンジ"
        assert to_katakana("chie") == u"チエ"
        assert to_katakana("tie") == u"チエ"
        assert to_katakana("kyouju") == u"キョウジュ"
        assert to_katakana("syuukyou") == u"シュウキョウ"
        assert to_katakana("shuukyou") == u"シュウキョウ"
        assert to_katakana("saichuu") == u"サイチュウ"
        assert to_katakana("saityuu") == u"サイチュウ"
        assert to_katakana("cheri-") == u"チェリー"
        assert to_katakana("tyeri-") == u"チェリー"
        assert to_katakana("shinrai") == u"シンライ"
        assert to_katakana("sinrai") == u"シンライ"
        assert to_katakana("hannnou") == u"ハンノウ"
        assert to_katakana("han'nou") == u"ハンノウ"
        
        assert to_katakana("wo") == u"ヲ"
        assert to_katakana("we") == u"ウェ"
        assert to_katakana("du") == u"ヅ"
        assert to_katakana("she") == u"シェ"
        assert to_katakana("di") == u"ヂ"
        assert to_katakana("fu") == u"フ"
        assert to_katakana("ti") == u"チ"
        assert to_katakana("wi") == u"ウィ"
        
        assert to_katakana("je") == u"ジェ"
        assert to_katakana("e-jento") == u"エージェント"
        
    def test_to_hiragana(self):
        assert to_hiragana("kanji") == u"かんじ"
        assert to_hiragana("kanzi") == u"かんじ"
        assert to_hiragana("kannji") == u"かんじ"
        assert to_hiragana("chie") == u"ちえ"
        assert to_hiragana("tie") == u"ちえ"
        assert to_hiragana("kyouju") == u"きょうじゅ"
        assert to_hiragana("syuukyou") == u"しゅうきょう"
        assert to_hiragana("shuukyou") == u"しゅうきょう"
        assert to_hiragana("saichuu") == u"さいちゅう"
        assert to_hiragana("saityuu") == u"さいちゅう"
        assert to_hiragana("cheri-") == u"ちぇりー"
        assert to_hiragana("tyeri-") == u"ちぇりー"
        assert to_hiragana("shinrai") == u"しんらい"
        assert to_hiragana("sinrai") == u"しんらい"
        assert to_hiragana("hannnou") == u"はんのう"
        assert to_hiragana("han'nou") == u"はんのう"
        
    def test_to_kana(self):
        assert to_kana("kanji") == u"カンジ"
        assert to_kana("kanzi") == u"カンジ"
        assert to_kana("kannji") == u"カンジ"
        assert to_kana("chie") == u"チエ"
        assert to_kana("tie") == u"チエ"
        assert to_kana("kyouju") == u"キョウジュ"
        assert to_kana("syuukyou") == u"シュウキョウ"
        assert to_kana("shuukyou") == u"シュウキョウ"
        assert to_kana("saichuu") == u"サイチュウ"
        assert to_kana("saityuu") == u"サイチュウ"
        assert to_kana("cheri-") == u"チェリー"
        assert to_kana("tyeri-") == u"チェリー"
        assert to_kana("shinrai") == u"シンライ"
        assert to_kana("sinrai") == u"シンライ"
        assert to_kana("hannnou") == u"ハンノウ"
        assert to_kana("han'nou") == u"ハンノウ"
        
        assert to_kana("wo") == u"ヲ"
        assert to_kana("we") == u"ウェ"
        assert to_kana("du") == u"ヅ"
        assert to_kana("she") == u"シェ"
        assert to_kana("di") == u"ヂ"
        assert to_kana("fu") == u"フ"
        assert to_kana("ti") == u"チ"
        assert to_kana("wi") == u"ウィ"
        
        assert to_kana("je") == u"ジェ"
        assert to_kana("e-jento") == u"エージェント"
        
    def test_to_hepburn(self):
        assert to_hepburn("kannzi") == "kanji"
        assert to_hepburn("tie") == "chie"
        
        assert to_hepburn("KANNZI") == "kanji"
        assert to_hepburn("TIE") == "chie"
        
        assert to_hepburn("カンジ") == "kanji"
        assert to_hepburn("チエ") == "chie"
        
        assert to_hepburn("かんじ") == "kanji"
        assert to_hepburn("ちえ") == "chie"
        
    def test_to_kunrei(self):
        assert to_kunrei("kanji") == "kanzi"
        assert to_kunrei("chie") == "tie"
        
        assert to_kunrei("KANJI") == "kanzi"
        assert to_kunrei("CHIE") == "tie"
        
        assert to_kunrei("カンジ") == "kanzi"
        assert to_kunrei("チエ") == "tie"
        
        assert to_kunrei("かんじ") == "kanzi"
        assert to_kunrei("ちえ") == "tie"
        
    def test_to_roma(self):
        assert to_roma(u"カンジ") == "kanji"
        assert to_roma(u"チャウ") == "chau"
        assert to_roma(u"ハンノウ") == "han'nou"
        
        assert to_roma(u"かんじ") == "kanji"
        assert to_roma(u"ちゃう") == "chau"
        assert to_roma(u"はんのう") == "han'nou"
        
    def test_is_consonant(self):
        assert not is_consonant("a")
        assert is_consonant("k")
        
    def test_is_vowel(self):
        assert is_vowel("a")
        assert not is_vowel("z")
        
    def test_expand_consonant(self):
        assert sorted(expand_consonant("k")) == ['ka', 'ke', 'ki', 'ko', 'ku']
        assert sorted(expand_consonant("s")) == ['sa', 'se', 'si', 'so', 'su']
        assert sorted(expand_consonant("t")) == ['ta', 'te', 'ti', 'to', 'tu']
        
        assert sorted(expand_consonant("ky")) == ['kya', 'kyo', 'kyu']
        assert sorted(expand_consonant("kk")) == ["kka", "kke", "kki", "kko", "kku"]
        assert sorted(expand_consonant("sh")) == ["sha", "she", "shi", "sho", "shu"]
        assert sorted(expand_consonant("sy")) == ["sya", "sye", "syo", "syu"]
        assert sorted(expand_consonant("ch")) == ["cha", "che", "chi", "cho", "chu"]
