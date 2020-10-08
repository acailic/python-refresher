#def add(x, y):
#    return x+y
# (lambda x,y: x+y)(5,7)
add = lambda x,y: x+y

print(add(5,7))

def double(x):
    return x*2


sequence=[1,3,5]
doubled = [double(x) for x in sequence]
doubled = map(double,sequence)

doubled = [(lambda x: x*2)for x in sequence]
doubled = map(lambda x: x*2,sequence)
# to print it needs to go to list(map())