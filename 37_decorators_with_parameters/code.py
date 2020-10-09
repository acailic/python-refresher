import functools

user = {"username": "Coa", "access_level": "guest"}
#admin = {"username": "Coa", "access_level": "admin"}


def make_secure(acces_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == acces_level:
                return func(*args, **kwargs)
            else:
                print(f"no {acces_level} permissions for {user['username']}")
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_pass():
    return "adminpass123"



@make_secure("guest")
def get_dashboard_pass():
    return "user:user_pass"


print(get_admin_pass())
print(get_dashboard_pass())
#print(get_admin_pass.__name__)


user = {"username": "Coa", "access_level": "admin"}
print(get_dashboard_pass())
print(get_admin_pass())
