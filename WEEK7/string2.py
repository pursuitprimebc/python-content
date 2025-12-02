'''QUESTION - Check if an even-length string has A or a in the second half
Given an even-length string s, check if the second half contains the character "a" or "A". Return True if it does, otherwise return False.

Example

s = "abcDef"
The second half is "Def", which does not contain "a" or "A", so the result is False.
'''
#PLATFORM - IITM COURSE

def has_a_in_second_half(s: str) -> bool:
     mid_point = len(s) // 2 
    second_half = s[mid_point:]
    
    return 'a' in second_half or 'A' in second_half
    


