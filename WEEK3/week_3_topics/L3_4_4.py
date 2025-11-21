# find wheather the entered number is palindrome or not

num = int(input('enter number:'))
absnum = abs(num)
rev = absnum%10
absnum = absnum // 10
while(absnum>0):
    r = absnum % 10
    absnum = absnum // 10
    rev = rev*10+r
if (num >= 0):
    print(rev)
else:
    rev2=rev - 2*rev
    print(rev2)

if (rev == num or rev2 == num):
    print('palindrome')
else:
    print('not a palindrome')    
