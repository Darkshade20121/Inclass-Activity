import pytest
import wordcount

def test_wordcount_pass():
    assert wordcount.count("Hello from the other side") == 5

def test_wordcount_pass_2():
    assert wordcount.count("Hello, World. How are you??") == 5

def test_wordcount_fail():
    assert wordcount.count("Hello,World") == 2
