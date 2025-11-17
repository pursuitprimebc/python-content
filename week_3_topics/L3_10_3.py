
'''here we do not the number iterations required it all 
depends upon the user input so these type of cases while loop
is ideal.
but  this can be solved using (for loop) for that we have to 
use foreach feature of for looop.
 '''

num = int(input('enter number:'))
'''absnum = abs(num)
rev = absnum%10
absnum = absnum // 10
while(absnum>0):
    r = absnum % 10
    absnum = absnum // 10
    rev = rev*10+r
if (num >= 0):
    print(rev)
else:
    print(rev - 2*rev)'''

absStrnum = str(abs(num))
rev = ''
for c in absStrnum:
    rev = c + rev
if (num>0):
    print(rev)
else:
    print('-' + rev)