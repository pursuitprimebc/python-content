# myString = "Chaf"
# myString_new = myString.replace('a', 'e')  
# print(myString_new)
# word = "Ocygen"
# word_new = word.replace('c', 'x').replace('g', 'y')
# print(word_new)

# str1 = "abcdef ghijkl"
# str2 = str1[2:1:-1]
# print(str2)
# # Complete the code to solve the task
# text = "Playground"
# str=text[2:7:-1]
# print(str)

words = input().split()
print(' '.join(words))


alpha='abcdefghijklmnopqrstuvwxyz'
i=25
s='jkrctvachvgtfcachvgtvqooqttqykpfctdjcpic' 
t=''
i=0
k=2
a = len(s)
for h in range(a):
    t=t+(alpha[(((alpha.index(s[i+h]))-k)%26)])
    print(t)






