import sys
sys.path.append('C:\\Users\\jianx\\Python Workfolder\\learning python\\CS50 Python Folder\\')

from week2.plates import is_valid

def test_number_at_end():
    assert is_valid("AB12C") == False
    assert is_valid("ABCD12") == True

def test_punctuation():
    assert is_valid("ABC,1") == False

def test_first_number_zero():
    assert is_valid("ABC012") == False
    assert is_valid("ABC210") == True

def test_length_of_plate():
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True

def test_start_two_letters():
    assert is_valid("A12345") == False
    assert is_valid("AB1234") == True
