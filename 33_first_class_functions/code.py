from operator import itemgetter
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cant be zero.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Couldnt find an element with {expected}.")


friends = [
    {"name": "coa", "age": 23},
    {"name": "Bob", "age": 22},
    {"name": "Raf", "age": 21}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Bob", get_friend_name))
#print(search(friends, "Bob", lambda friend: friend["name"]))
print(search(friends,"Bob", itemgetter("name")))

