def add_numbers(a, b):
    return a + b

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def reverse_string(text):
    return text[::-1]

def longest_word(words):
    if not words:
        return None
    return max(words, key=len)

def find_substring(str1, str2):
    if not str2:
        return 0
    return str1.find(str2)

def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]

def has_more_than_10_unique_chars(s):
    return len(set(s)) > 10