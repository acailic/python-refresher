def hello():
    print("hello!")


hello()

def users_age_in_seconds():
    user_age=int(input("Enter your age:"))
    age_seconds= user_age*365*24*60*60
    print(f"Your age in seconds is {age_seconds}.")


users_age_in_seconds()

#shadowing variable in different scope
friends = ["Coa", "Marko"]
def add_friend():
    friend_name=input("Enter you friend name:")
    friends = friends + [friend_name]

add_friend()


def submit_friend():
    thefriends.append("hehe")

thefriends= []

add_friend()
add_friend()
add_friend()
print(thefriends)


