'''QUESTION - Even Characters first and Odd Characters reversed
Given a string, return a string with the characters in the even indices first and the characters in the odd indices next but in reversed order.

Example For the input "abcde",

even chars = "ace"
odd chars = "bd"; odd chars reversed = "db"
result = "acedb"
'''
# PLATFORM - IITM course

def even_first_odd_reversed(s: str) -> str:
    even_chars = ""
    odd_chars = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]
            
    return even_chars + odd_chars[::-1]