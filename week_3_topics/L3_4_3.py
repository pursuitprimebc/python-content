# reverse the digits

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
    print(rev - 2*rev)