import pytest
import palidrome

def test_one_pass():
    assert palidrome.palidrome("racecar") == True

def test_two_pass():
    assert palidrome.palidrome("mom") == True

def test_one_fail():
    assert palidrome.palidrome("RACECAr") == True
