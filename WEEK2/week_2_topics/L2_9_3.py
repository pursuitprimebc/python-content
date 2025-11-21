# find the grade of the students based on the given mars from 0 to 100

marks=int(input('enter marks:'))

if (100>=marks >= 90):
    print('A')
elif (90>marks>=80):
    print('B')
elif (80>marks>=70):
    print('C')
elif (70>marks>=60):
    print('D')
elif (60> marks >=0):
    print('E')
else:
    print('invalid input')