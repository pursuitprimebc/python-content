print('travel from city A to city B')
time=int(input('enter time'))
longer_time=int(input('define longer'))
if (time>=longer_time):
    price=int(input('enter price:'))
    higher = int(input('define higher'))
    if (price>=higher):
        print('train')
    else:
        print('coach')    
else:
    price=int(input('enter price:'))
    higher = int(input('define higher'))
    if (price>=higher):
        print('Daytime flight')
    else:
        print('Red Eye Flight') 
print('Arrive city B')               
    