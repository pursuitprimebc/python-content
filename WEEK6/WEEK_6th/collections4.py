'''QUESTIONS - Set of Unique vowels in a string.
Given a string, return a set of unique vowels present in the string.

Examples

>>> unique_vowels('banana treat')
{'a', 'e'}
>>> unique_vowels('apple lolipop')
{'a', 'e', 'i', 'o'}
'''
# PLATFORM - IITM course 

def unique_vowels(s: str) -> set:
    vowels = set('aeiouAEIOU')
    return {char for char in s if char in vowels}
    