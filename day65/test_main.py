from main import *

def test_do_operation():
    assert do_operation("cube", 3) == 27
    assert do_operation("cube", -1) == -1


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True

def test_two_sum_sorted():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    assert two_sum_sorted([1, 2], 3) == [1, 2]


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("") == 0


def test_product_except_self():
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    assert product_except_self([0,1,2,3]) == [6,0,0,0]
    assert product_except_self([0,0,3,4]) == [0,0,0,0]