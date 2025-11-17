# difference btw for and while loop
num= int(input('enter number:'))
fact = 1
if (num<0):
    print('not defined')
else:
    '''while (num>0):
        fact = fact * num
        num = num-1
    print(fact)'''
    for i in range(num,1,-1):
        fact *= i
    print(fact)

'''for loop is Best when the number of iterations or  
   items is predetermined.
and while loop Best when continuation depends on 
    changing conditions.'''




