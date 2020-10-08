def named(**kwargs):
    print(kwargs)


def named(name, age):
    print(name, age)


named(name="bob", age=22)

details = {"name": "bob", "age": 22}
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Coa", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Aco", age=28)

""" 
def post(url,data=None, json=None, **kwargs):
    return request('post',url,data=data,**kwargs)
"""

myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error
