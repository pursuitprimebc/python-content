# string methods
a = 'Bibhash chandra Bishu'
x = '123ab'
p = '-----python-----'
b = 'python'

print(a.lower()) # coverts into lower case
print(a.upper()) # converts into upper case
print(a.capitalize()) # convetrs the first chracter to upper case
print(a.title()) #converts the first character of ech word to upper case
print(a.swapcase()) #swaps cases

print(a.islower()) # returns true if all characters in the string are lower case
print(a.isupper()) # returns true if all characters in the string are upper case
print(a.istitle())# returns true if the string follows thw rules of a title 

print(x.isdigit()) # returns true if all character in the string are digits
print(x.isalpha())# returns true is all character in the string are in alphabet
print(x.isalnum()) # returns true if all charcter in the string are alpha-numeric

print(p.strip('-')) # returns a trimmed version of the string
print(p.lstrip('-'))# returns a left trimmed version of string
print(p.rstrip('-'))# returns a right trimmed version of string

print(b.startswith('p'))# returns true is string starts with specified value (case sensetive)
print(b.endswith('N'))# returns true is string ends with specified value (case sensetive)

print(a.count('s'))
print(a.count('B'))
print(a.index('s'))
print(a.index('a'))

print(a.replace('B','b'))