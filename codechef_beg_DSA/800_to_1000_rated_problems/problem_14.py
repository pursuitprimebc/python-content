''' QUESTION - Is it a VOWEL or CONSONANT
Write a program to take a character (C) as input and check whether the given character is a vowel or a consonant.
NOTE: Vowels are 'A', 'E', 'I', 'O', 'U'. Rest all alphabets are called consonants.

Input Format
First line will contain the character C.
Output Format
Print "Vowel" if the given character is a vowel, otherwise print "Consonant".
'''


vowel = ['A','E','I','O','U']
c = input()
if c in vowel:
    print('vowel')
else:
    print('Consonant')


