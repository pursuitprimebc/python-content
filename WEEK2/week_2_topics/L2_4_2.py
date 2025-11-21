# deleting a variable

# x = 10
# print(x)
# del x
# print(x)

# shorthands for arithematic operators (+= , -= , *= , /=)

count = 0
count = count + 1
count += 1 
print(count)

count = 10
count = count - 1
count -= 1 
print(count)

count = 10
count = count * 2
count *= 2 
print(count)

count = 10
count = count / 2
count /= 2 
print(count)

# in operator
print('alpha' in 'a variable name can only contain alpha-numeric character and uderscore')
 
print('alpha' in 'a variable name must start with a letter the underscore character')

# when we use multiple relational operators in single statemnet then it is called s chaining operator.
x = 5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x>4)