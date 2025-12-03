'''QUESTION - Most frequent first letter of a word in a multiline passage.
Given a multi-line passage where the words are separated by spaces, find the letter which occurs most frequently as the first letter of any word. Consider both uppercase and lowercase letters as the same and return the letter in lowercase.

Assume there will be only one letter that occurs the most number of times as the first letter of a word.

Example:

passage = '''
word1 Word2 word3 word4 text1 text2
text3 Text4 word5 text5 word6
python1 python2 Python3
'''
The function will return "w" because "w" is the most frequently occurring first letter.
'''
#PLATFORM - IITM course

def most_occuring_first_letter(passage: str) -> str:
    
    first_letter_count = {}
    words = passage.split()
    
    for word in words:
        if word:
            first_letter = word[0].lower()
            first_letter_count[first_letter] = first_letter_count.get(first_letter, 0) + 1
            
    most_frequent_letter = max(first_letter_count, key=first_letter_count.get)
    
    return most_frequent_letter
    