x= (5,11) #brackets are not necessary
x= [(5,11)]
t= 8,9
d,f=t
a = t
print(a)
print(d,f)
people = [
    ("Bob",42,"Mechanic"),
    ("Roff",22,"Doctor"),
    ("Dani",32,"IT"),
          ]

for name,age,proffesion in people:
    print(f"{name} , {age}, {proffesion}")

for person in people:
    print(f"{person[0]} , {person[1]}, {person[2]}")

person = ("Bob",42,"IT")
name,_,proffesion= person
print(name,proffesion)

head, *tail = [1,2,3,4,5]
print(head)
print(tail)


