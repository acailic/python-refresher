def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 2, 3))

def add(x, y):
    return x+y

nums = [3, 5]
print(add(*nums))

dictionary = {"x":3, "y":4}
## named paramed used
print(add(**dictionary))

def apply(*args, operator):
    if operator =="*":
        return multiply(*args)
    elif operator =="+":
        return sum(args)
    else:
        print("No function for given operator")

print(apply(1,2,3,operator="*"))

