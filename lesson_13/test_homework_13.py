
import pytest
from homework_13 import (
    add_numbers, average, reverse_string,
    longest_word, find_substring, filter_strings,
    has_more_than_10_unique_chars
)

# Task 2
def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    with pytest.raises(TypeError):
        add_numbers(2, "3")


# Task 3
def test_average_positive():
    assert average([2, 4, 6]) == 4

def test_average_negative():
    assert average([]) is None


# Task 4
def test_reverse_string_positive():
    assert reverse_string("Привіт") == "тівирП"

def test_reverse_string_negative():
    assert reverse_string("") == ""


# Task 5
def test_longest_word_positive():
    assert longest_word(["кіт", "собака", "динозавр"]) == "динозавр"

def test_longest_word_negative():
    assert longest_word([]) is None


# Task 6
def test_find_substring_positive():
    assert find_substring("Hello, world!", "world") == 7

def test_find_substring_negative():
    assert find_substring("Hello", "cat") == -1


# Task 9
def test_filter_strings_positive():
    assert filter_strings(['1', 2, 'три']) == ['1', 'три']

def test_filter_strings_negative():
    assert filter_strings([1, 2, 3]) == []


# Task 10
def test_unique_chars_positive():
    assert has_more_than_10_unique_chars("abcdef123456") is True

def test_unique_chars_negative():
    assert has_more_than_10_unique_chars("aabbcc") is False