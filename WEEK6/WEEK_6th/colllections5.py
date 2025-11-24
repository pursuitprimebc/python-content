''' QUESTION - Sorted string with common characters from two strings.
Write a function to return a sorted string with unique common charecters present in the given two strings.

Examples

>>> common_char_sorted_str('apple', 'ball')
'al'
>>> common_char_sorted_str('abcde', 'edfci')
'cde'
'''
# PLATFORM - IITM course

def common_char_sorted_str(s1:str, s2:str) -> str: 
      common_chars = set(s1) & set(s2)
    return ''.join(sorted(common_chars))
    