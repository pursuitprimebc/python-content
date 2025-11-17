s='good'
print(s*5)
print(s[0]*5)


x='India'
print(x=='india') # python is case sensative
print(x=='India')
 
# for multi line comment use '''

'''String comparison checks each character from left 
to right until it finds a difference. The result is
True if the first non-equal character in the first 
string comes before the corresponding character in the 
second string (for <), and False otherwise.'''

print('apple' > 'one') # a comes before o so its false
print('four' < 'ten') #  

print('ab' < 'az') 
print('abcdef' < 'abcde') # f cannot be less than nothing