import functools
user = {"username": "Coa", "access_level": "guest"}
admin = {"username": "Coa", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if admin["access_level"] == "admin":
            return func
        else:
            print("no admin permissions")

    return secure_function


@make_secure
def get_admin_pass():
    return "123"


print(get_admin_pass())
print(get_admin_pass.__name__)
