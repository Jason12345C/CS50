import sys
sys.path.append('C:\\Users\\jianx\\Python Workfolder\\learning python\\CS50 Python Folder\\')

from week1.bank import value

def test_hello():
    assert value("hello, man") == "0"

def test_start_h():
    assert value("hi") == "20"

def test_anything_else():
    assert value("lol") == "100"

def test_upper():
    assert value("HELLO MAN") == "0"
