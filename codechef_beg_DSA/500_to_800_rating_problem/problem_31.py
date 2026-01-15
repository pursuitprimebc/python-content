'''QUESTION - Bus Seat Numbering
There is a bus with 30 seats. The seats are numbered from 1 to 30, and the numbering is as depicted in this image.


As can be seen in the image, the bus is divided into two decks - The Lower deck, and the Upper deck, with 15 seats each. And some of the seats come as Single and some as Double. For example, Seats 1 and 2 are Double, whereas Seat 11 is a Single.

You will be given a Seat number, and your job is to classify it as one of these 4 types:

Lower Single
Lower Double
Upper Single
Upper Double

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input which contains a single integers N — the seat number.

Output Format
For each test case, output on a new line, the type of seat.
'''


t = int(input())
for i in range(t):
    n = int(input())
    if n<=15:
        if n<=10:
            print('Lower Double')
        else:
            print('Lower Single')
    else:
        if n<=25:
            print('Upper Double')
        else:
            print('Upper Single')
    
