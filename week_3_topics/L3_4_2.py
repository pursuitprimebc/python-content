# find the number of digits inthe given number

num=abs(int(input('enter number:')))
digits = 1
while (num>9):
    num = num//10
    digits = digits + 1
print(digits)
 
# second method

'''num=abs(int(input('enter number:')))
digits = len(str(num))
print(digits)'''