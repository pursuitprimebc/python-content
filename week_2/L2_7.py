# this is popularly called tha caesar cipher in cryptography

alpha='abcdefghijklmnopqrstuvwxyz'
i=25
#print(alpha[i%26])
#print(alpha[(i+1)%26])
#print(alpha[(i+2)%26])
#print(alpha[(i+3)%26])

s='jkrctvachvgtfcachvgtvqooqtqykpfctdjcpic' # i expect to output tvebstibo

t=''
i=0
k=2
a = len(s)

for h in range(a):
    t=t+(alpha[(((alpha.index(s[i+h]))-k)%26)])
'''t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+5]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+6]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+7]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+8]))+k)%26)])'''
print(t)