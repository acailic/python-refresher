import functools

user = {"username": "Coa", "access_level": "guest"}
admin = {"username": "Coa", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if admin["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print("no admin permissions")

    return secure_function


@make_secure
def get_admin_pass(panel):
    if panel == "admin":
        return "123"
    elif panel == "billing":
        return "super_secure_pass"


print(get_admin_pass())
print(get_admin_pass.__name__)
