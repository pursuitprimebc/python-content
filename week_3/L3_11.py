# nested for loop

s ='VIBGYOR'
t ='VIBGYOR'
count = 0
for i in range(7):
    for j in range(7):
        print(f'{i}{j}{s[i]}{t[j]}')
        count = count +1                   

print('the total ways in which the 2 brothers can wear 7 different colours :',count)


