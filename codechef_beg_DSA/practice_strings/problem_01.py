''' QUESTION - DNA Storage
For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:

00 is replaced with A
01 is replaced with T
10 is replaced with C
11 is replaced with G
Given a binary string S of length N (N is even), find the encoded sequence.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains two lines of input.
First line contains a single integer N, the length of the sequence.
Second line contains binary string S of length N.
Output Format
For each test case, output in a single line the encoded sequence.

Note: Output is case-sensitive.
'''


t = int(input())

while t > 0:
    n = int(input())
    s = input()
    t -= 1
    dna_seq = ''
    dna_code = {
        '00':'A',
        '01':'T',
        '10':'C',
        '11':'G'
    }
    i = 0
    while n > 0:
        code = s[i:i+2]
        if  code in dna_code:
            dna_seq = dna_seq + dna_code[code]
        i = i+2
        n-=1
    
    print(dna_seq)
