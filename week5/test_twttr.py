import sys
sys.path.append('C:\\Users\\jianx\\Python Workfolder\\learning python\\CS50 Python Folder\\')
from week2.twttr import shorten


def test_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("hello, jason") == "hll, jsn"


def test_upper_case():
    assert shorten("HELLO") == "HLL"
    assert shorten("HELLO, JASON") == "HLL, JSN"

def test_mixed_case(): 
    assert shorten("LoUiE") == "L"

def test_leading_spaces(): 
    assert shorten("I am 20") == "m 20"

def test_numbers():
    assert shorten("1234567890") == "1234567890"