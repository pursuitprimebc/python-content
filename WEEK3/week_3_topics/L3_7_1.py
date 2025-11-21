# loop for multiplication tables

n = int(input('enter a number:'))

for i in range(1,11):
    # print(n,'X',i,'=',n*i)


# secondary method from L3_9
# FORMATTED PRINTING
# there is only one single string and inside curly braces variables r +nt
# second way to print statement mentioned above
    
    # print(f'{n} X {i} = {n*i}')

# another way
   # print('{0} X {1} = {2}'.format(n, i,n*i)) 

# another way ( using string modulo operator)
    print('%d X %d = %d' % (n,i,n*i))

