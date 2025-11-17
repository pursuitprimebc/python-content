# find the number of digits inthe given number
''' here we do not the number iterations required it all 
depends upon the user input so these type of cases while loop
is ideal.
but  this can be solved using (for loop) for that we have to 
use foreach feature of for looop.
 '''

num=abs(int(input('enter number:')))
'''digits = 1
while (num>9):
    num = num//10'''
strnum = str(num)
digits = 0
for a in strnum :   
    digits = digits + 1
print(digits)
 