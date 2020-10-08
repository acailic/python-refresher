l =["Aca","Daca","Zarko"]
t= ("Aca","Daca","Zarko") #cant modify tuple
s= {"Aca","Daca","Zarko"} #set no dupl

print(l[0]) #subscript notation
print(t[2])
#print(s[0])
l[0]="hehhe"
print(l)
l.append("Smith")
print(l)

l.remove("Daca")
s.add("Opa")
s.add("Opa")
print(s)
