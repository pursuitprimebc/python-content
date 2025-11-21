# find wheather the entered number is palindrome or not

num = int(input('enter number:'))
strabsnum = str(abs(num))
'''rev = absnum%10
absnum = absnum // 10
while(absnum>0):
    r = absnum % 10
    absnum = absnum // 10
    rev = rev*10+r
if (num<0):
    rev = rev-2*rev'''
rev = ''
for c in strabsnum:
    rev = c + rev
if (num<0):
    rev = '-'+ rev

if (int(rev) == num):
    print('palindrome')
else:
    print('not a palindrome')    
