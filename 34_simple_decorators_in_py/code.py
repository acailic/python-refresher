user = {"username": "Coa", "access_level": "guest"}
admin = {"username": "Coa", "access_level": "admin"}


def get_admin_pass():
    return "123"


def make_secure(func):
    def secure_function():
        if admin["access_level"] == "admin":
            return func
        else:
            print("no admin permissions")

    return secure_function


get_admin_pass = make_secure(get_admin_pass)

print(get_admin_pass())
