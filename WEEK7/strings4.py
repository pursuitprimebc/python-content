'''QUESTION - Remove First two and Last two Chars from a string
Given a string s, return a new string with the first two and last two characters removed.

If the string has less than four characters return an empty string.

Example

s = 'HelloWorld'
Removing the first two and last two characters results in 'lloWor'.
'''
# PLATFORM - IITM Course

def remove_edges(s: str) -> str:
    
    if len(s) < 4:
        return ""
        
    return s[2:-2]
    


