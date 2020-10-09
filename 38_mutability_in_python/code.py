a = []

b = a

a.append(23)
print(id(a))
print(id(b))

# all is mutable

# tuples are immutable, integers, strings, booleans
a = ()
b = ()
a = a + (15, 3)

c = 23
d = 23
#optimization, same id
print(id(c))
print(id(d))

f= "aca"
d= f
f+="world"
print(d)
print(f)