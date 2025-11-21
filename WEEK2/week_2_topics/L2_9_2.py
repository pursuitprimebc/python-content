# find whether the gieven number ends with o or 5 or any other num

print('enter number:')
num=int(input())

if (num%5==0):
    if(num%10==0):
        print('0')
    else:
        print('5')
else:
    print('other')
    

