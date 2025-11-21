# different ways to import a library
'''import calendar

# print(calendar.month(2025,10))
print(calendar.calendar(2025))'''

'''from calendar import month, calendar # if want to use more feature of calendar lib so we should use *
print(month(2025,10 ))
print(calendar(2025))'''

from calendar import month as m  
print(m(2025,10 ))

import calendar as c
print(c.month(2025,9))