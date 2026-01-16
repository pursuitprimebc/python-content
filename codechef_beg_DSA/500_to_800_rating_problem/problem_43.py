'''QUESTION - Complementary Strand in a DNA
You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,C, and G only.

Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequene of the complementary strand of the DNA.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains an integer N - denoting the length of string S.
Second line contains N characters denoting the string S.
Output Format
For each test case, output the string containing N characters - sequence of nucleotides of the complementary strand.
'''


t = int(input())
for i in range(t):
    n=int(input())
    s=input()
    complementary_strand = ""
    for i in range(n):
        if s[i]=='A':
            complementary_strand += "T"
        elif s[i]=='T':
            complementary_strand += "A"
        elif s[i]=='C':
            complementary_strand += "G"
        else:
            complementary_strand += "C"
    
    print(complementary_strand)



# this above code was written by me but this below code was that which i learned during solving , both are correct but below one is more concise.

'''
Suggestions for Improvement:

Use a Dictionary for Nucleotide Mapping: Instead of using multiple if/elif/else statements, you can use a dictionary to map each nucleotide to its complement. 
This makes the code more concise and easier to read.

String Concatenation: String concatenation in Python can be slow if done repeatedly inside a loop. Using join is more efficient. However, for strings of length up to 100, 
the performance difference is negligible, so you can keep the current approach if you prefer readabilit
'''

def solve():
    n = int(input())
    s = input()
    
    nucleotide_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    complementary_strand = ''.join(nucleotide_map[nucleotide] for nucleotide in s)
    print(complementary_strand)

t = int(input())
for _ in range(t):
    solve()

'''
Key changes:

A dictionary nucleotide_map is used to store the complements of each nucleotide.
A list comprehension [nucleotide_map[nucleotide] for nucleotide in s] is used to create a list of complementary nucleotides.
''.join() is used to join the list of characters into a string.
'''



