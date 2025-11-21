# type conversion ( float - int , str - int)


a = int(6.32)
b = int('10')

print(a, type(a))
print(b, type(b))

# type conversion ( int - float , str - float)

e = float(6)
d = float('1.3456')

print(e, type(e))
print(d, type(d))

# type conversion ( int - str , float - str)

f = str(6)
s = str(1.3456)

print(f, type(f))
print(s, type(s))

# type conversion ( int - str , float - str)
# only zero will return boolean false other than that all are true

q = bool(10)
w = bool(0)
r = bool(-10)
t = bool(3.45)
y = bool(0.0)
u = bool(-56.78)

print(q, type(q))
print(w, type(w))
print(r, type(r))
print(t, type(t))
print(y, type(y))
print(u, type(u))

# all strings are converted true bool value except empty str

p = bool('india')
o = bool('0')
i = bool('-10.4') 
k = bool('')

print(p, type(p))
print(o, type(o))
print(i, type(i))
print(k, type(k))