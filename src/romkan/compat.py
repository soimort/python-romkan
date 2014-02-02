import sys
import string

PY2 = sys.version_info[0] <= 2

letters = string.letters if PY2 else string.ascii_letters
if PY2:
    from unicodecsv import DictReader
    unichr = unichr
    unicode = unicode
else:
    from csv import DictReader
    unichr = chr
    unicode = str
