users = [
    ("Bob", 42, "bob1"),
    ("Roff", 22, "roff2"),
    ("Dani", 32, "dani1"),
]

username_mapping = {user[0]: user for user in users}

username_input = input("Enter your username:")
password_input = input("Enter your password:")

username, _, password = username_mapping[username_input]


if password_input == password:
    print("Your details are correct!")
else:
    print("Incorrect details.")