import re
from romkan.data import ROMKAN, katakana, hiragana
from romkan.compat import letters


def is_consonant(c):
    """
    Return a MatchObject if a Latin letter is a consonant in Japanese.
    Return None otherwise.
    """
    return re.match("[ckgszjtdhfpbmyrwxn]", c.lower())


def is_vowel(c):
    """
    Return a MatchObject if a Latin letter is a vowel in Japanese.
    Return None otherwise.
    """
    return re.match("[aeiou]", c.lower())


def expand_consonant(c):
    """
    Expand consonant to its related moras.
    Example: 'sh' => ['sha', 'she', 'shi', 'sho', 'shu']
    """
    c = c.lower()    
    return sorted([mora for mora in ROMKAN.keys() if re.match("^%s.$" % c, mora)])


def is_romaji(text):
    return all([c in letters for c in text])


def is_katakana(text):
    return all([c in katakana for c in text])


def is_hiragana(text):
    return all([c in katakana for c in text])


def is_kana(text):
    return all([c in katakana or c in hiragana for c in text])
