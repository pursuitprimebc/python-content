''' QUESTION - Area OR Perimeter
Write a program to obtain length (L) and breadth (B) of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

Input Format
First line will contain the length (L) of the rectangle.
Second line will contain the breadth (B) of the rectangle.
Output Format
Output 2 lines.

In the first line print "Area" if area is greater otherwise print "Peri" and if they are equal print "Eq".(Without quotes).

In the second line print the calculated area or perimeter (whichever is greater or anyone if it is equal).
'''



l = int(input())
b = int(input())
area = l*b 
perimeter = 2*(l+b)
if area>perimeter:
    print('area')
    print(area)
elif perimeter>area:
    print('peri')
    print(perimeter)
else:
    print('Eq')
    print(area)



