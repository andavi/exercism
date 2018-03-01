import re


def is_pangram(sentence):
    return len(set(''.join(re.findall('[a-z]*', sentence.lower())))) == 26
